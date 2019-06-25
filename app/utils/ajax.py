from flask import jsonify, make_response


def not_found(err_msg=''):
    return jsonify({
        'errMsg': err_msg
    }), 404


def internal_server_error():
    pass


def bad_request():
    pass


def gone():
    pass
