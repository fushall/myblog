from app import create_app as _create_app
from models import db, drop_all, create_all
from models.user import UserModel
from models.post import PostModel
from models.tag import TagModel


def create_app():
    app = _create_app()

    @app.shell_context_processor
    def make_shell_context():
        return dict(
            app=app,
            db=db,
            drop_all=drop_all,
            create_all=create_all,
            UserModel=UserModel,
            PostModel=PostModel,
            TagModel=TagModel
        )

    print(app.url_map)
    print(app.config)
    return app
