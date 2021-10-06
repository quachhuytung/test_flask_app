from http import HTTPStatus

from . import app
from infrastructures.response import write_not_found_response, write_success_response
from app.models import Post
from app.serializers import PostSchema
from dto.post_schema import index_page_fields

@app.route('/hello')
def hello():
    return write_success_response(message="Hello")

@app.route('/posts')
def get_all_post():
    posts = Post.query.all()
    post_schema = PostSchema(many=True, only=index_page_fields)
    return write_success_response(data=post_schema.dump(posts))

@app.errorhandler(HTTPStatus.NOT_FOUND)
def invalid_route(e):
    return write_not_found_response()