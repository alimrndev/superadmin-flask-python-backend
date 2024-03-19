from flask import jsonify, make_response

def success(values, message):
    res = {
        'data': values,
        'message': message,
        'status' : 200
    }

    return make_response(jsonify(res)), 200

def badRequest(values, message):
    res = {
        'data': values,
        'message': message,
        'status' : 400
    }

    return make_response(jsonify(res)), 400

def internalServerError():
    res = {
        'message': 'Terjadi kesalahan internal server!',
        'status' : 500
    }

    return make_response(jsonify(res)), 500
