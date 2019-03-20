import os
from flask import Flask, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./movies.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
session = db.session

################set up Models##################
collections = db.Table('collections',db.Column('director_id',db.Integer, db.ForeignKey('directors.id')),db.Column('genre_id',db.Integer, db.ForeignKey('genres.id')))

class Director(db.Model):
    __tablename__ = "directors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    nationality = db.Column(db.String(64))
    genres = db.relationship('Genre',secondary=collections,backref=db.backref('directors',lazy='dynamic'),lazy='dynamic')
    movies = db.relationship('Movie',backref='Director')

    def __repr__(self):
        return "{} (ID: {})".format(self.name,self.id)


class Genre(db.Model):
    __tablename__ = "genres"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    movies = db.relationship('Movie',backref='Genre')

    def __repr__(self):
        return "{} (ID: {})".format(self.name,self.id)

class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    nationality = db.Column(db.String(64))
    Runningtime = db.Column(db.Integer)
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"))
    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"))


    def __repr__(self):
        return self.title


##########helper functions############

def get_or_create_director(director_name):
    director = Director.query.filter_by(name=director_name).first()
    if director:
        return director
    else:
        director = Director(name=director_name)
        session.add(director)
        session.commit()
        return director


def get_or_create_genre(genre_name):
    genre = Genre.query.filter_by(name=genre_name).first()
    if genre:
        return genre
    else:
        genre = Genre(name=genre_name)
        session.add(genre)
        session.commit()
        return genre


#############route funcions######################
@app.route('/',methods=["GET", "POST"])
def index():
    movies = Movie.query.all()
    num_movies = len(movies)
    return render_template('index.html',num_movies=num_movies)


@app.route('/movie/new/<title>/<director>/<genre>')
def new_movie(title,director,genre):
    if Movie.query.filter_by(title=title).first():
        return "That movie already exists! Go back to the main app!"
    else:
        director = get_or_create_director(director)
        genre = get_or_create_genre(genre)
        movie = Movie(title = title, director_id = director.id,genre_id = genre.id)
        session.add(movie)
        session.commit()
        return "New movie: {} by {}. Check out the URL for ALL movies to see the whole list.".format(movie.title, director.name)

@app.route('/all_movies')
def see_all():
    all_movies = []
    movies = Movie.query.all()
    for m in movies:
        director = Director.query.filter_by(id=m.director_id).first() # get just one artist instance
        genre = Genre.query.filter_by(id=m.genre_id).first()
        all_movies.append((m.title,director.name,genre.name))
    return render_template('all_movies.html',all_movies=all_movies)


@app.route('/all_directors')
def see_all_directors():
    directors = Director.query.all()
    names = []
    for d in directors:
        num_movies = len(Movie.query.filter_by(director_id=d.id).all())
        newtup = (d.name,num_movies)
        names.append(newtup) # names will be a list of tuples
    return render_template('all_directors.html',director_names=names)


if __name__ == '__main__':
    db.create_all()
    app.run()
