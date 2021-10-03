from http import HTTPStatus

from . import app
from infrastructures.response import write_not_found_response, write_success_response

@app.route('/hello')
def hello():
    return write_success_response(message="Hello")

@app.errorhandler(HTTPStatus.NOT_FOUND)
def invalid_route(e):
    return write_not_found_response()