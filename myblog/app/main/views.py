from flask import render_template, g, request

from . import blueprint
from models.post import PostModel, get_post, get_posts
from models.tag import TagModel, get_tag_byname
from models.user import UserModel


@blueprint.route('/test')
def test():
    return render_template('main/test.html')


@blueprint.route('/')
def index():
    user = UserModel.query.get(1)
    _posts = get_posts(desc=True)
    tags = TagModel.query.all()
    return render_template('main/index.html', posts=_posts, tags=tags, user=user)


@blueprint.route('/post/<int:post_id>')
def post(post_id):
    _post = get_post(post_id)
    return render_template('main/post.html', post=_post)


@blueprint.route('/post')
def posts():
    tag_name = request.args.get('tag', '', str)
    if tag_name is not None:
        tag = get_tag_byname(tag_name)
        _posts = tag.posts
    else:
        _posts = get_posts()
    return render_template('main/posts.html', tag_name=tag_name, posts=_posts)
