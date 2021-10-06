from flask import Blueprint

from app.models import Post
from app.serializers import PostSchema
from dto.post_schema import post_fields

from infrastructures.response import write_success_response, write_not_found_response

post_pages_bp = Blueprint("post_pages", __name__)

@post_pages_bp.route('/', strict_slashes=False)
def get_all_post():
    posts = Post.query.all()
    post_schema = PostSchema(many=True, only=post_fields)
    return write_success_response(data=post_schema.dump(posts))


@post_pages_bp.route('/<post_id>')
def get_post_by_id(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post:
        post_schema = PostSchema(only=post_fields)
        return write_success_response(data=post_schema.dump(post))
    else:
        return write_not_found_response(message=f'Post id {post_id} not found')