#search_movie.py

from tables import Movie, Genre
import pandas as pd

# Function to get movies and save in a data frame
def get_movie_df(session):
    movies = session.query(Movie).all()
    movie_data = [
        {
            "id":movie.id,
            "title":movie.title,
            "description":movie.description,
            "rating":movie.rating,
            "release_year":movie.release_year
        } for movie in movies
    ]
    movie_df = pd.DataFrame(movie_data)
    return movie_df

# Function to save searched movies
def collect_movies(sesseion):
    while True:
        print("-----------------------------------------------------------------")
        print("1. Add to watch in the future")
        print("2. Add to currently watching list")
        print("3. Add to watched list")
        print("0. Done")
        choice = input("Choose an option: ")
        if choice == "1":
            print("Added to the future watching list")
        elif choice == "2":
            print("Added to the future watching list")
        elif choice == "3":
            print("Added to the future watching list")
        elif choice == "0":
            break
        else:
            print("Invalid option! Try again.")

# Function to get top ten most rated movies
def get_best_movies(session):
    print("-----------------------------------------------------------------")
    print("10 BEST MOVIES")
    print("-----------------------------------------------------------------")
    movie_df = get_movie_df(session)
    print(movie_df.loc[:9,["id", "title", "rating", "release_year"]])
    print("-----------------------------------------------------------------")
    collect_movies(session)    

# Function to search movies by getting a title input
def search_by_title(session):
    title = input("Enter the movie title: ").title()
    found_movies = session.query(Movie).filter(Movie.title == title).all()
    if found_movies:
        print("Search Results: ")
        for movie in found_movies:
            print(f"id: {movie.id}, title: {movie.title}, rating: {movie.rating}, released: {movie.release_year}")
        collect_movies(session)
    else:
        print(f"'{title}' not found")

# Function to search movies by getting a genre input
def search_by_genre(session):
    search_genre = input("Enter a genre: ").title()
    genres = session.query(Genre).filter(Genre.genre_type == search_genre).first()
    if genres:
        movies = genres.movies
        if movies:
            print(f"Movies in {genres} genre........")
            for movie in movies:
                print(f"id: {movie.id}, title: {movie.title}, released: {movie.release_year}")
            # Option to add movies into individual list
            collect_movies(session)
        else:
            print(f"No movies found for {search_genre} genre.")
    else:
        print(f"'{search_genre}' genre not found.")

# Function to search; search menu
def search(session):
    while True:
        print("-----------------------------------------------------------------")
        print("1. Best 10 Movies")
        print("2. Search by Movie Title")
        print("3. Search by Genre")
        print("0. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            get_best_movies(session)
        elif choice == "2":
            search_by_title(session)
        elif choice == "3":
            search_by_genre(session)
        elif choice == "0":
            break
        else:
            print("Invalid option! Try again.")

if __name__ == "__main__":
    search()