from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from . import blueprint
from .forms import LoginForm
from app.models.user import UserModel


@blueprint.route('/')
@login_required
def index():
    return render_template('admin/index.html')


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print(form.data)
    if form.validate_on_submit():
        user = UserModel.query.filter_by(name=form.username.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user, remember=form.remember.data)
            flash('脸上笑嘻嘻:)')
        else:
            flash('滚蛋！( o｀ω′)ノ')
        return redirect(url_for('admin.index'))

    return render_template('admin/login.html', form=form)


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('拜拜')
    return redirect(url_for('admin.login'))
