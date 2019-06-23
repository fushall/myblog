from flask import session
from werkzeug.security import check_password_hash
import config


def check_user_hash(username, password):
    return username == config.USERNAME and check_password_hash(config.PASSWORD, password)


def user_logined():
    return check_user_hash(session.get('username', ''), session.get('password', ''))
