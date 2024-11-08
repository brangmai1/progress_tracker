from user import sign_up, log_in 
from search_movie import search_movies
from tables import User, Movie
import sys

def setup_user(session):
    while True:
        print()
        print("1. Sign up")
        print("2. Sign in")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            print("Signing up...")
            user = sign_up(session)
            if user is not None:
                search_movies(user, session)
                profile_setting(user, session)
        elif choice == '2':
            user = log_in(session)
            if user is not None:
                profile_setting(user, session)
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# User profile function; the landing page for a user
def profile_setting(user, session):    
    # Admin's options
    if user.role == 'admin':
        print("\n1. View movie lists")
        print("2. Manage Users")
        print("3. Edit Profile")
        print("0. Sign Out")
        choice = input("Choose an option: ")
        if choice == "1":
            display_movie_lists(user, session)
        elif choice == "2":
            print("1. View users")
            print("2. Delete users")
            print("0. Done")
            admin_choice = input("Choose an option: ")
            if admin_choice == "1":
                view_all_users(user, session)
                profile_setting(user, session)
            elif admin_choice == "2":
                delete_user(user, session)
                profile_setting(user, session)
            else:
                profile_setting(user, session)
        elif choice == "3":
            edit_list(user, session)  
        else:
            print("Goodbye!")
            sys.exit()
    # User's options
    elif user.role == 'user':
        print("\n1. View movie lists")
        print("2. Edit my movie list")
        print("0. Sign Out")
        choice = input("Choose an option: ")
        if choice == "1":
            display_movie_lists(user, session)
        elif choice == "2":
            edit_list(user, session)  
        else:
            print("Goodbye!")
            sys.exit()

# Display user's movie lists
def display_movie_lists(user, session):
    user_profile = session.query(User).filter(User.username == user.username).first()
    watching_movies = user_profile.watching_list
    future_movies = user_profile.to_watch_list
    watched_movies = user_profile.watched_list

    # Print movies that are on the watching list.
    print("\n-----------------------------------------------------------------------------")
    print("CURRENTLY WATCHING MOVIES")
    print("-----------------------------------------------------------------------------")
    
    if not watching_movies:
        print("No movies listed.")
    else:
        for movie in watching_movies:
            print(f"id: {movie.id}, title: {movie.title}, genre: {movie.rating}, released: {movie.release_year}")
    
    # Print movies that are on the future list.
    print("\n-----------------------------------------------------------------------------")
    print("MOVIES TO WATCH IN THE FUTURE")
    print("-----------------------------------------------------------------------------")
    if not future_movies:
        print("No movies listed.")
    else:
        for movie in future_movies:
            print(f"id: {movie.id}, title: {movie.title}, genre: {movie.rating}, released: {movie.release_year}")
    
    # Print movies that are on the watched list.
    print("\n-----------------------------------------------------------------------------")
    print("WATHCHED MOVIES")
    print("-----------------------------------------------------------------------------")
    if not watched_movies:
        print("No movies listed.")
    else:
        for movie in watched_movies:
            print(f"id: {movie.id}, title: {movie.title}, genre: {movie.rating}, released: {movie.release_year}")
    profile_setting(user, session)


# Function that a user can manage their accounts
def edit_list(user, session):
    print("\n1. Add movies")
    print("2. Remove movies")
    print("3. Update progress status")
    print("0. Done")
    choice = input("Choose an option: ").strip()
    if choice == "1":
        # Search movies to add to the lists
        search_movies(user, session)
    elif choice == "2":
        # Delete movie from one of users' lists
        remove_movie(user, session)
    elif choice == "3":
        # Update movie from one of users' lists
        update_list(user, session)        
    elif choice == "0":
        profile_setting(user, session)
    else:
        print("\nInvalid option! Try again.")
    profile_setting(user, session)

# Function to select user's lists: currently watching, to watch in the future or watched lists
def select_list(user):
    while True:
        print("1. Currently watching list")
        print("2. future watch list")
        print("3. Watched list")
        choice = input("Choose an option: ")
     
        if choice == "1":
            return user.watching_list
        elif choice == "2":
            return user.to_watch_list
        elif choice == "3":
            return user.watched_list
        else:
            print("Invalid option. Try again.")

# Function to remove a movie from a user's list, then add the movie to a different list
def update_list(user, session):
    # Update movies from one of users' lists
    print("\nMovie list to update from:")
    update_movie_from = select_list(user)
    movie_id_to_update = int(input("Movie ID to update: "))
    print("\nMovie list to update to:")
    update_movie_to = select_list(user)
    movie = session.query(Movie).filter(Movie.id == movie_id_to_update).first()
    if not movie or movie not in update_movie_from:
        print(f"Movie ID {movie_id_to_update} not found")
    else:
        update_movie_from.remove(movie)
        if movie in update_movie_to:
            print(f"Movie ID {movie_id_to_update} is already on the list")
        else:
            update_movie_to.append(movie)   
            session.commit()
            print(f"\nMovie ID: {movie_id_to_update} is updated.")


# Function to add a movie to the user's one of three lists: future watch, watching and watched lists.
def add_movie(users_list, movie_id, session):
    movie_to_add = session.query(Movie).filter(Movie.id == movie_id).first()
    if movie_to_add not in users_list:
        users_list.append(movie_to_add)
        session.commit()
    else:
        print(f"\nMovie ID: {movie_id} is already on {users_list}")

# Function to remove a movie from one of the user's lists
def remove_movie(user, session):
    print("\nMovie list to remove from:")
    movie_list = select_list(user)
    movie_id_to_delete = int(input("Movie ID to delete: "))
    delete(movie_list, movie_id_to_delete, session)
    print(f"\nMovie ID: {movie_id_to_delete} is removed.")

# Function to delete a movie from the user's one of three lists: future watch, watching and watched lists.
def delete(users_list, movie_id, session):
    movie_to_delete = session.query(Movie).filter(Movie.id == movie_id).first()
    if movie_to_delete in users_list:
        users_list.remove(movie_to_delete)
        session.commit()
    else:
        print("Movie not found.")

def view_all_users(user, session):
    if user.role != 'admin':
        raise PermissionError("Access Denied: Admins only.")
    all_users = session.query(User).all()
    for user in all_users:
        print(f"username: {user.username}, email: {user.email}")

def delete_user(session):
    username = input("Enter username to remove: ")
    user_to_delete = session.query(User).filter(User.username == username).first()
    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()
    else:
        print(f"Username: {username} not found.")

        
        



