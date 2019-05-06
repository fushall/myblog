flask_debug_run:
    export FLASK_APP=myblog/manage.py
    export FLASK_ENV=development
    export FLASK_DEBUG=1
    flask run