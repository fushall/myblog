from pkgutil import iter_modules
from importlib import import_module
from warnings import warn

from flask import url_for

from .tag import tagmaker
from .register import fetch_blueprints, fetch_libcdns


class LibraryManager:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app

        from . import __path__
        for module in iter_modules(prefix=f'{__package__}.', path=__path__):
            if module.ispkg is True and module.name.startswith('_') is False:
                import_module(f'{module.name}')

        blueprints = fetch_blueprints()
        for blueprint in blueprints.values():
            self.app.register_blueprint(blueprint)

        self.app.jinja_env.globals['library'] = self

    def __call__(self, filepath, cdn_libname=None, cdn_libversion=None, cdn_libfilename=None):
        try:
            libname, libver, libfilename = filepath.split('/')
        except ValueError:
            warn('文件路径填写错误', stacklevel=2)
            make_tag = tagmaker('')
            return make_tag()

        if self.app.debug is False:
            libname = libname if cdn_libname is None else cdn_libname
            libver = libver if cdn_libversion is None else cdn_libversion
            libfilename = libfilename if cdn_libfilename is None else cdn_libfilename

        url = None
        if self.app.debug:
            url = url_for(f'library_{libname}.static', filename=f'{libver}/{libfilename}')
        else:
            libcdns = fetch_libcdns()
            libcdn = libcdns.get(libname)
            if libcdn:
                url = libcdn.format(name=libname, version=libver, filename=libfilename)

        make_tag = tagmaker(url)
        return make_tag()

