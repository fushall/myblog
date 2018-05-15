from app import create_app as __create_app
from app.models import db, drop_all, create_all
from app.models.user import UserModel, create_user


def create_app():
    app = __create_app()

    @app.shell_context_processor
    def make_shell_context():
        return dict(
            app=app,
            db=db,
            drop_all=drop_all,
            create_all=create_all,
            UserModel=UserModel,
            create_user=create_use r
        )

    print(app.url_map)
    print(app.config)
    return app
