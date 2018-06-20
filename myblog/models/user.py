"""
myblog是单人博客，user即admin
"""


from . import db, Mixin

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from utils import markdown2html


class UserModel(db.Model, Mixin, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(16), nullable=False, unique=True)  # 用户名
    password_hash = db.Column(db.Unicode(128), nullable=False)     # 密码哈希值
    info_html = db.Column(db.UnicodeText)                          # 主页个人信息栏
    raw_markdown = db.Column(db.UnicodeText)                       # 原生markdown

    @property
    def password(self):
        raise AttributeError('不要尝试获取密码')

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


def get_user(user_id: int):
    user = UserModel.query.get(int(user_id))
    return user


def get_user_byname(user_name):
    return UserModel.query.filter_by(name=user_name).first()


def create_user(name, password, markdown="他什么都没写  "):
    user = UserModel(
            name=name,
            password=password,
            info_html=markdown2html(markdown),
            raw_markdown=markdown
        )
    return user.save()
