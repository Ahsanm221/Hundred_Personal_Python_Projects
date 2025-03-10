from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


HEADERS = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3MGVkNzE5MDMxNDZmNTg2NzFjNjA2ZGYwNmQzNjI0ZiIsInN1YiI6IjY0O"
                     "GRiOThmYzJmZjNkMDBhZDAxYzA5NiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.5fZVK22jGKy20nL_TW2"
                     "90ofZFZVKPGUWZ3PUG0Vkd4c"
}
URL = "https://api.themoviedb.org/3/search/movie"
APIKEY = "70ed71903146f58671c606df06d3624f"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top_10_movies.db"
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()

# new_movie = Movie( title="Phone Booth", year=2002, description="Publicist Stuart Shepard finds himself trapped in a
# phone booth, pinned down by an extortionist's " "sniper rifle. Unable to leave or receive outside help,
# Stuart's negotiation with the caller leads to " "a jaw-dropping climax.", rating=7.3, ranking=10, review="My
# favourite character was the caller.", img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg" )


@app.route("/")
def home():
    # all_movies = db.session.execute(db.select(Movie)).scalars()
    # This line creates a list of all the movies sorted by rating
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


class RateMovieFrom(FlaskForm):
    rating = StringField('Your rating out of 10 e.g. 7.5')
    review = StringField('Your review')
    submit = SubmitField('Done')


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieFrom()
    movie_id = request.args.get("id")
    movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, movie=movie)


@app.route('/delete')
def delete():
    movie_id = request.args.get("id")
    movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


class AddMovie(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


@app.route('/add', methods=["GET", "POST"])
def add():
    add_form = AddMovie()
    if add_form.validate_on_submit():
        movie_title = add_form.title.data
        response = requests.get(URL, headers=HEADERS, params={"api_key": APIKEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template('add.html', form=add_form)


@app.route('/find', methods=["GET", "POST"])
def find_movie():
    movie_id = request.args.get("id")
    movie_api_details_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(movie_api_details_url, headers=HEADERS, params={"api_key": APIKEY, "language": "en-US"})
    data = response.json()
    new_movie = Movie(
        title=data["original_title"],
        year=data["release_date"].split("-")[0],
        description=data["overview"],
        img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
