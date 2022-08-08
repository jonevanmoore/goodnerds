from .db import db

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    portrait = db.Column(db.String)
    bio = db.Column(db.String)


def to_dict(self):
    return {
        'id': self.id,
        'first_name': self.first_name,
        'last_name': self.last_name,
        'portrait': self.portrait,
        'bio': self.bio
    }
