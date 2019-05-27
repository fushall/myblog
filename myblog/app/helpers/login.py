from flask import session
from utils.login import check_user_hash


def user_logined():
    return check_user_hash(session.get('username', ''), session.get('password', ''))
