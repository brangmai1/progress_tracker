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
def collect_movies(user, movie_id, session):
    movie_to_save = session.query(Movie).filter(Movie.id == movie_id).first()
    if movie_to_save:
        # User can save movies into three different lists: to watch in the future, watching now or watched.
        print("-----------------------------------------------------------------------------")
        print("1. Add to currently watching list")
        print("2. Add to watch in the future")
        print("3. Add to watched list")
        print("0. Done")
        choice = input("Choose an option: ")
        # Option to save a movie to the future watch list
        if choice == "1":
            # Check the movie to save is already on the list
            if movie_to_save not in user.watching_list:
                user.watching_list.append(movie_to_save)
                session.commit()
                print(f"{movie_to_save.title} is dded to the future watching list")
            else:
                print(f"{movie_to_save.title} is already on the watching list.")
            
        # Option to save a movie to the currently watching list
        elif choice == "2":
            # Check the movie to save is already on the list
            if movie_to_save not in user.to_watch_list:
                user.to_watch_list.append(movie_to_save)
                session.commit()
                print(f"{movie_to_save.title} is added to the future watching list")
            else:
                print(f"{movie_to_save.title} is already on future watch list.")
            
        # Option to save a movie to the watched list
        elif choice == "3":
            # Check the movie to save is already on the list
            if movie_to_save not in user.watched_list:
                user.watched_list.append(movie_to_save)
                session.commit()
                print(f"{movie_to_save.title} added to the future watching list")
            else:
                print(f"{movie_to_save.title} is already on the watched list.")
        elif choice == "0":
            return
        else:
            print("Invalid option! Try again.")
    else:
        print(f"Movie id: {movie_id} not found.")

# Function asking user to save movies
def save_movie():
    save = input("Do you want to add movies to your lists? y/n :")
    return save.lower() == 'y'

# Function to get top ten most rated movies
def get_best_movies(user, session):
    print("\n--------------------------------------------------------------------------")
    print("BEST MOVIES OF ALL TIME")
    print("\n--------------------------------------------------------------------------")
    movie_df = get_movie_df(session)
    row_start = 0
    row_end = 9

    while True:
        print("\n--------------------------------------------------------------------------")
        print(movie_df.loc[row_start:row_end,["id", "title", "rating", "release_year"]])
        print("\n--------------------------------------------------------------------------")
        while save_movie():
            movie_id = int(input("Enter a movie ID: "))
            collect_movies(user, movie_id, session) 

        print("\n1. More")
        print("2. Back")
        print("0. Done")
        choice = input("Choose option:")   
        if choice == '1':
            row_start += 10
            row_end += 10
            if row_start > (movie_df.size - 10):
                print("End of movie list.")
                break
        elif choice == '2':
            row_start -= 10
            row_end -= 10
            if row_start < 0:
                print("End of movie list.")
                break
        else:
            break

# Function to search movies by getting a title input
def search_by_title(user, session):
    title = input("\nEnter the movie title: ").title()
    found_movies = session.query(Movie).filter(Movie.title == title).all()
    if found_movies:
        print("Search Results: ")
        for movie in found_movies:
            print(f"id: {movie.id}, title: {movie.title}, rating: {movie.rating}, released: {movie.release_year}")
        if save_movie():
            movie_id = int(input("Enter movie id to save it: "))
            collect_movies(user, movie_id, session)    
    else:
        print(f"'{title}' not found")

# Function to search movies by getting a genre input
def search_by_genre(user, session):
    search_genre = input("\nEnter a genre: ").title()
    genres = session.query(Genre).filter(Genre.genre_type == search_genre).first()
    if genres:
        movies = genres.movies
        if movies:
            print(f"Movies in {genres} genre........")
            for movie in movies:
                print(f"id: {movie.id}, title: {movie.title}, released: {movie.release_year}")
            # Option to add movies into individual list
            if save_movie():
                movie_id = int(input("Enter a movie id to save it: "))
                collect_movies(user, movie_id, session)    
        else:
            print(f"No movies found for {search_genre} genre.")
    else:
        print(f"'{search_genre}' genre not found.")


# Function to search; search menu
def search_movies(user, session):
    while True:
        print("\n--------------------------------------------------------------------------")
        print("1. View Best Movies")
        print("2. Search by Movie Title")
        print("3. Search by Genre")
        print("0. Back")
        choice = input("Choose an option: ")
        if choice == "1":
            get_best_movies(user, session)
        elif choice == "2":
            search_by_title(user, session)
        elif choice == "3":
            search_by_genre(user, session)
        elif choice == "0":
            return
        else:
            print("Invalid option! Try again.")
