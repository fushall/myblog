import os
from datetime import timedelta

# 随便输入一个secret_key
SECRET_KEY = 'thisisthesecretkey'
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres@localhost:5432/myblog'

# session 过期时间，主要给username 和 password 用
PERMANENT_SESSION_LIFETIME = timedelta(hours=2)
USERNAME = os.environ['myblog_username']
PASSWORD = os.environ['myblog_password']
