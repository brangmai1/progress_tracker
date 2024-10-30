from user import sign_up, log_in 
from search_movie import search
from tables import User, Movie

def setup_user(session):
    while True:
        print()
        print("1. Sign up")
        print("2. Sign in")
        print("0. Sign out")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            print("Signing up...")
            user = sign_up(session)
            if user is not None:
                search(user, session)
        elif choice == '2':
            user = log_in(session)
            if user is not None:
                profile(user, session)
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


def profile(user, session):
    user_profile = session.query(User).filter(User.username == user.username).first()
    watching_movies = user_profile.watching_list
    future_movies = user_profile.to_watch_list
    watched_movies = user_profile.watched_list
    print("\n-----------------------------------------------------------------------------")
    print("CURRENTLY WATCHING MOVIES")
    print("-----------------------------------------------------------------------------")
    if not watching_movies:
        print("No movies currently watching.")
    else:
        for movie in watching_movies:
            print(f"id: {movie.id}, title: {movie.title}, genre: {movie.rating}, released: {movie.release_year}")
    print("\n-----------------------------------------------------------------------------")
    print("MOVIES TO WATCH IN THE FUTURE")
    print("-----------------------------------------------------------------------------")
    if not future_movies:
        print("No movies to watch in the future.")
    else:
        for movie in future_movies:
            print(f"id: {movie.id}, title: {movie.title}, genre: {movie.rating}, released: {movie.release_year}")
    print("\n-----------------------------------------------------------------------------")
    print("WATHCHED MOVIES")
    print("-----------------------------------------------------------------------------")
    if not watched_movies:
        print("No watched movies listed.")
    else:
        for movie in future_movies:
            print(f"id: {movie.id}, title: {movie.title}, genre: {movie.rating}, released: {movie.release_year}")
    edit_list(user, session)  

def edit_list(user, session):
    print("1. Add movies")
    print("2. Remove movies")
    print("3. Update progress status")
    print("0. Exit")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        # Search movies to add to the lists
        search(user, session)
    elif choice == "2":
        # Delete movie from one of users' lists
        remove_movie(user, session)
    elif choice == "3":
        # Update movie from one of users' lists
        update_list(user, session)        
    elif choice == "0":
        return
    else:
        print("Invalid option! Try again.")

def select_list(user):
    while True:
        print("1. future watch list")
        print("2. Currently watching list")
        print("3. Watched list")
        choice = input("Choose an option: ")
     
        # future_movies = user.to_watch_list
        # watching_movies = user.watching_list
        # watched_movies = user.watched_list
        if choice == "1":
            return user.to_watch_list
        elif choice == "2":
            return user.watching_list
        elif choice == "3":
            return user.watched_list
        else:
            print("Invalid option. Try again.")

# Function to remove a movie from a user's list, then add the movie to a different list
def update_list(user, session):
    # Update movies from one of users' lists
        print("Choose a movie to update from:")
        update_movie_from = select_list(user)
        movie_id_to_update = input("Enter movie id to update: ")
        print("Choose a movie to update to:")
        update_movie_to = select_list(user)
        delete(update_movie_from, movie_id_to_update, session)
        add_movie(update_movie_to, movie_id_to_update, session)
        print(f"Movie ID: {movie_id_to_update} is updated.")


# Function to add a movie to the user's one of three lists: future watch, watching and watched lists.
def add_movie(users_list, movie_id, session):
    movie_to_add = session.query(Movie).filter(Movie.id == movie_id).first()
    if movie_to_add not in users_list:
        users_list.append(movie_id)
        session.commit()
    else:
        print(f"Movie ID: {movie_id} is already on {users_list}")

# Function to remove a movie from one of the user's lists
def remove_movie(user, session):
    print("Remove from list:")
    movie_list = select_list(user)
    movie_id_to_delete = input("Movie ID to delete: ")
    delete(movie_list, movie_id_to_delete, session)
    print(f"Movie ID: {movie_id_to_delete} is removed.")

# Function to delete a movie from the user's one of three lists: future watch, watching and watched lists.
def delete(users_list, movie_id, session):
    movie_to_delete = session.query(Movie).filter(Movie.id == movie_id).first()
    if movie_to_delete:
        users_list.remove(movie_to_delete)
        session.commit()
    else:
        print("Movie not found.")
        
        



