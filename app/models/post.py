from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Post id: {self.id}>'

    @classmethod
    def create(cls, name, email):
        ins = cls(name=name,email=email)
        db.session.add(ins)
        db.session.commit()
        return ins