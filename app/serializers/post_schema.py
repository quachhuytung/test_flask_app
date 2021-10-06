from app import ma
from app.models.post import Post 

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post