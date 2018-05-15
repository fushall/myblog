from flask import Flask

from app.configs import init_configs
from app.views import register_views
from app.models import db
from app.exts.library import LibraryManager



def create_app():
    #: 创建Flask实例对象
    app = Flask(__name__)

    #: 初始化配置
    init_configs(app)

    #: 初始化数据库
    db.init_app(app)

    #: 各种扩展
    #: [css, js 本地/cdn 切换器]
    from . import libraries
    LibraryManager(app, libraries)

    # 注册错误页面，蓝图
    register_views(app)

    return app
