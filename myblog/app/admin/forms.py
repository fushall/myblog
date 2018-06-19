from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField, FileField, TextAreaField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('账号', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember = BooleanField('记住登陆')


class UploadPostForm(FlaskForm):
    file = FileField('markdown文件', validators=[DataRequired()])


class ReplacePostForm(FlaskForm):
    text = StringField('确认？', validators=[DataRequired()])


class PreviewPostForm(FlaskForm):
    text = StringField('确认？', validators=[DataRequired()])


class DeletePostForm(FlaskForm):
    text = StringField('确认？', validators=[DataRequired()])


class UserInfoForm(FlaskForm):

    userinfo = TextAreaField('个人信息', validators=[DataRequired()])
