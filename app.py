from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
from connect_database import make_session
from search_movie import get_movie_df
from tables import User, Movie, Genre
import os
import pandas as pd
import re
from initial_setup import setup_table_data

ADMINS = ["brangmai@email.com"]
app = Flask(__name__)
app.secret_key = os.urandom(24) # Generates a 24-byte random key
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30) # Prevents stale connections for both flask and database sessions

@app.route("/", methods=["GET"])
def index():
    with make_session() as db_session:
        setup_table_data(db_session)
    # return render_template("index.html")
    return render_template("login.html")
    
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        # Render the login form
        return render_template("login.html")
    elif request.method == "POST":
        # Get data from the form
        username = request.form.get("username")
        password = request.form.get("password")

        with make_session() as db_session:
            user = db_session.query(User).filter(User.username == username).first()        
            if user and check_password_hash(user.password, password):   
                # Successful login, redirect to movies page   
                session["username"] = user.username   
                return redirect(url_for("home"))
            else:
                # Invalid login
                flash("Invalid credentials. Please try again.")
                return redirect(url_for("login"))
        
@app.route("/logout", methods=["POST"])
def logout():
    session.clear() # Clear Flask session
    flash("Logged out seuccessfully.")
    return redirect(url_for("login"))

        
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
       
        # Password validation check
        if len(password) < 8:
            flash("Password must be at least 8 characterslong.", "danger")
            return redirect(url_for("signup"))
        if not re.search(r"[A-Z]", password):
            flash("Password must contain at least one uppercase letter.", "danger")
            return redirect(url_for("signup"))
        if not re.search(r"[a-z]", password):
            flash("Password must contain at least one lowercase letter.", "danger")
            return redirect(url_for("signup"))
        if not re.search(r"[0-9]", password):
            flash("Password must contain at least one digit.", "danger")
            return redirect(url_for(signup))
        
        confirm_password = request.form.get("confirm_password")
        if password != confirm_password:
            flash("Passwords do not match.", "danger")
            return redirect(url_for("signup"))
        
        hash_password = generate_password_hash(password, method="pbkdf2:sha256", salt_length=16)
        name = request.form["name"]
        email = request.form["email"]
        with make_session() as db_session:
            # Check if username or email already already exists
            existing_user = db_session.query(User).filter((User.username==username) or (User.email == email)).first()
            if existing_user:
                flash("Username or email already exists. Please choose another.", "error")
                return redirect(url_for("signup"))
            new_user = User(username=username, password=hash_password, name=name, email=email)
            if new_user.email in ADMINS:
                new_user.role = "admin"
            db_session.add(new_user)
            db_session.commit()
            session["username"] = username
            flash("Sign-up successful!")
            return redirect((url_for("login")))        
    # Render the sign up form
    return render_template("signup.html")
    

@app.route("/home", methods=["GET", "POST"])
def home():
    username = session.get("username")
    if not username:
        flash("Please, log in")
        return redirect(url_for("login"))
    
    with make_session() as db_session:
        movies_df = get_movie_df(db_session)
        movies = movies_df.head(10).to_dict(orient="records")
        db_user = db_session.query(User).filter(User.username == username).first()
        currently_watching_movies = db_user.watching_list
        planned_watching_movies = db_user.to_watch_list
        watched_movies = db_user.watched_list
    return render_template("home.html", movies=movies, currently_watching_movies=currently_watching_movies, planned_watching_movies=planned_watching_movies, watched_movies=watched_movies)

@app.route("/search", methods=["GET"])
def search():
    search_type = request.args.get("search_type")
    query = request.args.get("query", "").strip().title()

    # Get the current page number from the query parameters - default is 1
    page = request.args.get("page", 1, type=int)
    movies_per_page = 15

    with make_session() as db_session:
        if search_type == "title":
            movies_query = db_session.query(Movie).filter(Movie.title.ilike(f"%{query}%"))
        elif search_type == "genre":
            genre = db_session.query(Genre).filter(Genre.genre_type.ilike(f"%{query}%")).first()
            if genre:
                # Convert list of movies to a query object
                movies_query = db_session.query(Movie).filter(Movie.id.in_([movie.id for movie in genre.movies]))
            else:
                movies_query = db_session.query(Movie).filter(False)  # Empty query
        else:
            # movies_df = get_movie_df(db_session)
            # movies = movies_df.head(10).to_dict(orient="records")
            movies_query = db_session.query(Movie)

        # Fetch total number of movies for pagination
        total_movies = movies_query.count()
        # Calculate the offset
        offset = (page - 1) * movies_per_page
        # Fetch the movies for the current page
        movies = movies_query.limit(movies_per_page).offset(offset).all()
        # Calculate total pages for the front-end pagination
        total_pages = (total_movies + movies_per_page - 1) // movies_per_page    
    return render_template("search.html", movies=movies, search_type=search_type, page=page, total_pages=total_pages, query=query)

@app.route("/movie/<int:movie_id>", methods=["GET"])
def movie_details(movie_id):
    with make_session() as db_session:
        movie = db_session.query(Movie).filter(Movie.id == movie_id).first()
        # If movie not found, return an error page
        if not movie:
            return "<h3>Movie not found</h3>", 404

        # Pass the referer URL (previous page) to the template
        previous_page = request.referrer # Capture the referring page URL    
        # Pass the movie details to the template
        return render_template("movie_details.html", movie=movie, previous_page=previous_page)

@app.route("/add_to_list", methods=["GET","POST"])
def add_to_list():
    # try:
    #     movie_id = request.form.get("movie_id")
    # except (TypeError, ValueError):
    #     flash("Inalid movie ID.", "Warning")
    #     return redirect(request.referrer)
    movie_id = request.form.get("movie_id")
    if movie_id:
        with make_session() as db_session:
            movie = db_session.query(Movie).filter(Movie.id == movie_id).first()
            if movie:
                username = session.get("username")
                user = db_session.query(User).filter(User.username == username).first()
                if movie not in user.to_watch_list:
                    user.to_watch_list.append(movie)
                    db_session.commit()
                    flash(f"{movie.title} has been added to your 'To Watch' list!", "Success")
                else:
                    flash(f"{movie.title} is already on the list", "info")
            else:
                flash("Movie not found.", "Error")
    else:
        flash("Invalid action.", "Warning")
    return redirect(request.referrer) # Redirect back to the previous page

if __name__ == "__main__":
    app.run(debug=True, port=5001)