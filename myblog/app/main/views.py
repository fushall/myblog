from . import blueprint

from flask import render_template, g

from models.post import PostModel
from models.tag import TagModel
from models.category import CategoryModel


@blueprint.route('/')
def index():
    posts = PostModel.query.order_by(PostModel.posted_at.desc()).all()
    tags = TagModel.query.all()
    categories = CategoryModel.query.all()
    return render_template('main/index.html', posts=posts, tags=tags, categories=categories)


@blueprint.route('/post/<int:post_id>')
def post(post_id):
    _post = PostModel.query.get(post_id)
    return render_template('main/post.html', post=_post)


