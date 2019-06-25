from importlib import import_module

from flask import Blueprint as _Blueprint, render_template
from werkzeug.utils import find_modules


class Blueprint(_Blueprint):
    bps = []

    def __init__(self, name, import_name, static_folder='static',
                 static_url_path=None, template_folder='templates',
                 url_prefix='/', subdomain=None, url_defaults=None,
                 root_path=None):
        super().__init__(name, import_name, static_folder,
                         static_url_path, template_folder,
                         url_prefix, subdomain, url_defaults,
                         root_path)
        self.bps.append(self)

    def render_template(self, template_name_or_list, **context):
        if isinstance(template_name_or_list, str):
            template_name_or_list = f'{self.name}/{template_name_or_list}'
        else:
            template_name_or_list = [f'{self.name}/{tn}' for tn in template_name_or_list]
        return render_template(template_name_or_list, **context)


def register_blueprints(app):
    # blueprint modules do not be imported by default,
    # so we have to import automatically by a for-loop
    for pkg in find_modules('app', include_packages=True):
        import_module(pkg)

    for bp in Blueprint.bps:
        app.register_blueprint(bp)
