from flask import render_template, request, redirect, url_for, flash, session, current_app
from flask_login import login_user, logout_user, login_required

from . import blueprint
from utils import markdown2html
from .forms import LoginForm, UploadPostForm, PreviewPostForm, DeletePostForm, ReplacePostForm, UserInfoForm
from models.user import get_user_byname
from models.post import create_post, get_posts
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
        markdown_file = request.files.get(form.file.name)
        try:
            temppost = create_post(markdown_file.stream)

            return redirect(url_for('admin.preview_post'))
        except UnicodeDecodeError:
            flash('要上传的博客仅支持utf8编码的md文件')
            return redirect(url_for('admin.upload_post'))
    return render_template('admin/upload_post.html', form=form)


@blueprint.route('/replace-post/<int:post_id>')
@login_required
def replace_post(post_id):
    current_app.replaced_post_id = post_id
    return redirect(url_for('admin.upload_post'))


@blueprint.route('/delete-post/<int:post_id>', methods=['POST', 'GET'])
@login_required
def delete_post(post_id):
    form = DeletePostForm()
    post = PostModel.query.get(post_id)
    if form.validate_on_submit() and form.text.data == '确认删除':
        if post:
            for tag in post.tags:
                if len(tag.posts) == 1:
                    tag.delete().commit()
            post.delete().commit()
        else:
            flash("ID不对，删不了")
        return redirect(url_for('admin.index'))
    return render_template('admin/delete_post.html', form=form, post=post)


@blueprint.route('/preview-post', methods=['POST', 'GET'])
@login_required
def preview_post():
    temp_post = current_app.temp_post
    if temp_post is None:
        flash('没传文章你预览什么？')
        return redirect(url_for('admin.index'))
    form = PreviewPostForm()
    if form.validate_on_submit() and form.text.data == '确认上传':

        replaced_post_id = temp_post['replaced_post_id']

        post = PostModel(
            id=replaced_post_id,
            title=temp_post['title'],
            summary_html=temp_post['summary_html'],
            maintext_html=temp_post['maintext_html'],
            raw_markdown=temp_post['raw_markdown']
        ).save()


        new = temp_post['tags']['new']
        repeated = temp_post['tags']['repeated']

        # 新标签
        for tagname in new:
            tag = TagModel(name=tagname, posts=[post]).save()

        # 已存在的标签
        for tagname in repeated:
            tag = TagModel.query.filter_by(name=tagname).first()
            tag.posts.append(post)
            tag.save()

        current_app.temp_post = None
        flash('上传成功！')
        return redirect(url_for('admin.index'))

    return render_template('admin/preview_post.html', form=form, temp_post=temp_post)


@blueprint.route('/userinfo', methods=['POST', 'GET'])
@login_required
def userinfo():
    form = UserInfoForm()
    user = UserModel.query.get(1)

    if form.validate_on_submit() and user:
        _userinfo = form.userinfo.data

        user.raw_markdown = _userinfo
        user.info_html = markdown2html(_userinfo)
        user.save()
        return redirect(url_for('admin.userinfo'))
    else:
        form.userinfo.data = user.raw_markdown
    return render_template('admin/userinfo.html', form=form, user=user)
