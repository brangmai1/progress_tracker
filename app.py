from flask import Flask, render_template, request
from connect_database import make_session
from search_movie import get_movie_df


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    with make_session() as session:
        movies_df = get_movie_df(session)
        movies = movies_df.head(10).to_dict(orient="records")
        return render_template("index.html", movies=movies)


if __name__ == "__main__":
    app.run(debug=True, port=5001)