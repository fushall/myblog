import os

from pkgutil import iter_modules
from importlib import import_module

from flask import Blueprint, url_for, abort
from .tag import tagmaker


class LibraryManager:
    def __init__(self, app=None):
        self.libs = {}
        self.app = None

        if app is not None:
            self.init_app(app)

    def register_lib(self, pkg):
        library = pkg.Library

        name = library.name
        cdn = library.cdn
        folder = os.path.join(pkg.__name__.split('.')[-1], library.folder)
        self.libs[name] = dict(folder=folder, cdn=cdn)

    def init_app(self, app):
        self.app = app

        from . import __path__
        for module in iter_modules(prefix=f'{__package__}.', path=__path__):
            if module.ispkg is True and module.name.startswith('_') is False:
                pkg = import_module(f'{module.name}')
                self.register_lib(pkg)

        blueprint = Blueprint('library', __name__, url_prefix='/library')

        @blueprint.route('/<path:filepath>')
        def static(filepath):
            name, filename = filepath.split('/', 1)
            blueprint.static_folder = self.libs[name]['folder']
            return blueprint.send_static_file(filename)

        self.app.register_blueprint(blueprint)
        self.app.jinja_env.globals['library'] = self

    def __call__(self, filepath):
        try:
            name, version, filename = filepath.split('/')

            if self.app.debug:
                url = url_for(f'library.static', filepath=f'{name}/{version}/{filename}')
            else:
                url = self.libs[name]['cdn'].format(name=name, version=version, filename=filename)

            make_tag = tagmaker(url)
            return make_tag()

        except ValueError:
            abort(404)
