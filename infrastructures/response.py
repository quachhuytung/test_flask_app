from http import HTTPStatus

from flask import make_response, jsonify

from constants.http_response.schema import BASE_RESPONSE_MESSAGE, \
    BASE_RESPONSE_DATA, DEFAULT_DATA, DEFAULT_MESSAGE, NOT_FOUND_MESSAGE

from constants.http_response.default_headers import DEFAULT_HEADERS


def add_headers(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        for k,v in DEFAULT_HEADERS.items():
            r.headers[k] = v
        return r
    return wrapper

@add_headers
def write_success_response(data=DEFAULT_DATA, message=DEFAULT_MESSAGE):
    response = make_response(jsonify({
        BASE_RESPONSE_MESSAGE: message,
        BASE_RESPONSE_DATA: data
    }), HTTPStatus.OK)
    return response

@add_headers
def write_not_found_response(message=NOT_FOUND_MESSAGE, data=DEFAULT_DATA):
    response = make_response(jsonify({
        BASE_RESPONSE_MESSAGE: message,
        BASE_RESPONSE_DATA: data
    }), HTTPStatus.NOT_FOUND)
    return response