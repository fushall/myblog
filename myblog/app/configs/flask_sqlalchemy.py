class Default:
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Development(Default):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:admin@localhost:3307/myblog?charset=utf8mb4'


class Production(Default):
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:admin@localhost/myblog?charset=utf8mb4'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:admin@localhost:3307/myblog?charset=utf8mb4'