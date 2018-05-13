from pkgutil import iter_modules
from importlib import import_module


def __register_blueprints(flask_app):
    for module in iter_modules(__path__):

        # 自动导入非下划线开头的蓝图package
        if module.ispkg and module.name.startswith('_') is False:
            blueprint_package = import_module(f'{__package__}.{module.name}')

            # 导入蓝图的视图
            import_module(f'{blueprint_package.__package__}.views')

            # 注册蓝图
            flask_app.register_blueprint(blueprint_package.blueprint)


def register_views(flask_app):
    __register_blueprints(flask_app)
