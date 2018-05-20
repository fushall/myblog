from . import blueprint

from flask import render_template, g
from markdown import markdown

from app.models.post import PostModel

code = '''
# 代码演示如下：

```python3
from app import create_app as __create_app
from app.models import db, drop_all, create_all
from app.models.user import UserModel, create_user


def create_app():
    app = __create_app()
    
    # 卧槽这什么贵什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊什么贵啊啊？
    # 6666 ???
    @app.shell_context_processor
    def make_shell_context():
        return dict(
            app=app,
            db=db,
            drop_all=drop_all,
            create_all=create_all,
            UserModel=UserModel,
            create_user=create_user
        )

    print(app.url_map)
    print(app.config)
    return app
```


'''


@blueprint.route('/')
def index():
    config = dict(
        codehilite=dict(
            use_pygments=False,
            css_class='prettyprint'
        )
    )
    md = markdown(code*3, extensions=['codehilite', 'fenced_code'], extension_configs=config)
    posts = PostModel.query.order_by(PostModel.posted_at.desc()).all()
    print(posts)
    return render_template('main/index.html', posts=posts)


@blueprint.route('/post/<int:post_id>')
def post(post_id):
    post = PostModel.query.get(post_id)
    return render_template('main/post.html', post=post)


