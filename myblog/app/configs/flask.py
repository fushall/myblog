from datetime import timedelta


class Default:
    SECRET_KEY = 'Welcome to my blog myblog!'


class Development(Default):
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)


class Production(Default):
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
