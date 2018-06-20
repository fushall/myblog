from flask import render_template, request, redirect, url_for, flash, session, current_app
from flask_login import login_user, logout_user, login_required

from . import blueprint
from utils import markdown2html
from .forms import LoginForm, UploadPostForm, PreviewPostForm, DeletePostForm, ReplacePostForm, UserInfoForm
from models.user import get_user_byname, get_user, set_userinfo
from models.post import create_post, get_post, get_posts, replace_post as _replace_post, delete_post as _delete_post
from models.tag import TagModel


@blueprint.route('/')
@login_required
def index():
    return render_template('admin/index.html', posts=get_posts())


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user_byname(form.username.data)
        if user and user.verify_password(form.password.data):
            login_user(user, remember=form.remember.data)
        else:
            flash('滚蛋！( o｀ω′)ノ')
        return redirect(url_for('admin.index'))
    return render_template('admin/login.html', form=form)


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.login'))


@blueprint.route('/upload-post', methods=['POST', 'GET'])
@login_required
def upload_post():
    form = UploadPostForm()

    if form.file.data:
        post_id = int(request.form.get('post_id'))
        markdown_file = request.files.get(form.file.name)
        try:
            temp_post = create_post(markdown_file.stream)
            if post_id:
                return redirect(url_for('admin.replace_post', src_post_id=temp_post.id, dist_post_id=post_id))
            else:
                return redirect(url_for('admin.preview_post', temp_post_id=temp_post.id))
        except UnicodeDecodeError:
            flash('要上传的博客仅支持utf8编码的md文件')
            return redirect(url_for('admin.upload_post'))
    return render_template('admin/upload_post.html', form=form, post_id=request.args.get('post_id', 0))


@blueprint.route('/replace-post', methods=['POST', 'GET'])
@login_required
def replace_post():
    form = ReplacePostForm()

    src_post = get_post(request.args.get('src_post_id'))
    dist_post = get_post(request.args.get('dist_post_id'))

    if form.validate_on_submit() and form.text.data == '确认替换':
        _replace_post(src_post, dist_post)
        flash('替换成功！')
        return redirect(url_for('admin.index'))
    return render_template('admin/replace_post.html', form=form, src_post=src_post, dist_post=dist_post)


@blueprint.route('/delete-post/<int:post_id>', methods=['POST', 'GET'])
@login_required
def delete_post(post_id):
    form = DeletePostForm()
    post = get_post(post_id)
    if form.validate_on_submit() and form.text.data == '确认删除':
        if post:
            _delete_post(post)
        else:
            flash("ID不对，删不了")
        return redirect(url_for('admin.index'))
    return render_template('admin/delete_post.html', form=form, post=post)


@blueprint.route('/preview-post/<int:temp_post_id>', methods=['POST', 'GET'])
@login_required
def preview_post(temp_post_id):
    temp_post = get_post(temp_post_id)
    if temp_post is None:
        flash('无法找到该临时文章？')
        return redirect(url_for('admin.index'))

    form = PreviewPostForm()
    if form.validate_on_submit() and form.text.data == '确认上传':

        temp_post.temperory = False
        temp_post.commit()

        flash('上传成功！')
        return redirect(url_for('admin.index'))

    return render_template('admin/preview_post.html', form=form, temp_post=temp_post)


@blueprint.route('/userinfo', methods=['POST', 'GET'])
@login_required
def userinfo():
    form = UserInfoForm()
    user = get_user(1)

    if form.validate_on_submit() and user:  # 有问题
        set_userinfo(user, form.userinfo.data)
        return redirect(url_for('admin.userinfo'))
    else:
        form.userinfo.data = user.raw_markdown
    return render_template('admin/userinfo.html', form=form, user=user)
