from flask import Flask, render_template, request, redirect, url_for
from connect_database import make_session
from search_movie import get_movie_df
from tables import User


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
    
@app.route("/login", methods=["POST"])
def login():
    # Get data from the form
    username = request.form["username"]
    password = request.form["password"]

    with make_session() as session:
        user = session.query(User).filter(User.username == username).first()        
        if user and user.password == password:   
            # Successful login, redirect to movies page         
            return redirect(url_for("display_movies"))
        else:
            # Invalid login
            return "Invalid credentials. Please try again."
        
@app.route("/movies", methods=["GET"])
def display_movies():
    with make_session() as session:
        movies_df = get_movie_df(session)
        movies = movies_df.head(10).to_dict(orient="records")
    return render_template("movies.html", movies=movies)


if __name__ == "__main__":
    app.run(debug=True, port=5001)