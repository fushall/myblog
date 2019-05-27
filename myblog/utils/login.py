from werkzeug.security import check_password_hash
import settings


def check_user_hash(username, password):
    return username == settings.USERNAME and check_password_hash(settings.PASSWORD, password)
