from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, URL, ValidationError


class CreateGenreForm(FlaskForm):
    book_genre = StringField('book_genre')


class CreateAuthorForm(FlaskForm):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    portrait = StringField('portrait')
    bio = StringField('bio')


class CreateBookForm(FlaskForm):
    author_id = StringField('author_id')
    genre_id = StringField('genre_id')
    title = StringField('title', validators=[DataRequired()])
    release_date = StringField('release_date', validators=[DataRequired()])
    summary = StringField('summary', validators=[DataRequired()])


class EditBookForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    release_date = StringField('release_date', validators=[DataRequired()])
    summary = StringField('summary', validators=[DataRequired()])


class CreateReviewForm(FlaskForm):
    user_id = StringField('user_id')
    book_id = StringField('book_id')
    rating = IntegerField('rating')
    title = StringField('title')
    content = StringField('content')


class EditReviewForm(FlaskForm):
    rating = IntegerField('rating')
    title = StringField('title')
    content = StringField('content')


class CreateStatusForm(FlaskForm):
    user_id = StringField('user_id')
    book_id = StringField('book_id')
    status = StringField('status')


class EditStatusForm(FlaskForm):
    status = StringField('status')
