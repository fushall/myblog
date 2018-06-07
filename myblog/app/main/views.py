from flask import render_template, g, request

from . import blueprint
from models.post import PostModel
from models.tag import TagModel


@blueprint.route('/')
def index():
    _posts = PostModel.query.order_by(PostModel.posted_at.desc()).all()
    tags = TagModel.query.all()
    return render_template('main/index.html', posts=_posts, tags=tags)


@blueprint.route('/post/<int:post_id>')
def post(post_id):
    _post = PostModel.query.get(post_id)
    return render_template('main/post.html', post=_post)


@blueprint.route('/post')
def posts():
    tag_name = request.args.get('tag', '', str)
    if tag_name is not None:
        tag = TagModel.query.filter_by(name=tag_name).first()
        _posts = tag.posts
    else:
        _posts = PostModel.query.all()
    return render_template('main/posts.html', tag_name=tag_name, posts=_posts)
