from app import create_app as __create_app
from model import db, drop_all, create_all
from model.user import UserModel, create_user
from model.post import PostModel
from model.tag import TagModel, TagsMapModel


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
            PostModel=PostModel,
            TagModel=TagModel,
            TagsMapModel=TagsMapModel,
            create_user=create_user
        )

    print(app.url_map)
    print(app.config)
    return app
