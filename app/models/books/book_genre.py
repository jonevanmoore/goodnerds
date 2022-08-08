from .db import db

class BookGenre(db.Model):
    __tablename__ = 'book_genres'

    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String)


def to_dict(self):
    return {
    'id': self.id,
    'genre': self.genre
    }
