from http import HTTPStatus

from . import app
from infrastructures.response import write_not_found_response
from app.modules.web import post_pages_bp

app.register_blueprint(post_pages_bp, url_prefix='/posts')

@app.errorhandler(HTTPStatus.NOT_FOUND)
def invalid_route(e):
    return write_not_found_response()