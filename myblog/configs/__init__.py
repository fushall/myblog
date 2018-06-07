from pkgutil import iter_modules
from importlib import import_module


def register_configs(app):
    for module in iter_modules(__path__):
        if module.ispkg is False and module.name.startswith('_') is False:
            config_module = import_module(f'{__package__}.{module.name}')

            if app.debug:
                config = config_module.Development
            else:
                config = config_module.Production
            app.config.from_object(config)
