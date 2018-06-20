from app import create_app as _create_app
from models import db, drop_all, create_all
from models.user import UserModel, create_user
from models.post import PostModel
from models.tag import TagModel


def create_db(app):
    create_all(app)


def drop_db(app):
    drop_all(app)


def create_app():
    app = _create_app()

    @app.shell_context_processor
    def make_shell_context():
        return dict(
            app=app,
            db=db,
            create_db=create_db,
            drop_db=drop_db,
            UserModel=UserModel,
            create_user=create_user,
            PostModel=PostModel,
            TagModel=TagModel
        )

    print(app.url_map)
    print(app.config)
    return app
