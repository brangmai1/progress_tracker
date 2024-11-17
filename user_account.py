from account_setting import sign_up, log_in, settings
from search_movie import search_movies, get_best_movies
from tables import User, Movie
from getpass import getpass
import sys

def setup_user(session):
    while True:
        print("\n1. Sign up")
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
    print("\n1. Search movies")
    print("2. View my movie lists")    
    print("3. Edit my movie list")
    print("4. Account settings")
    if user.role == "admin":
        print("5. Admin settings")
    print("0. Sign Out")
    choice = input("Choose an option: ")
    if choice == "1":
        # Search movies to add to the lists
        search_movies(user, session)
    elif choice == "2":        
        display_movie_lists(user, session)
    elif choice == "3":
        edit_list(user, session)  
    elif choice == "4":
        settings(user, session)
    elif choice == "5" and user.role == "admin":
        print("\n1. Manage users")
        print("2. manage movies")
        print("0. Done")
        admin_manage_choice = input("Choose a number option: ")
        if admin_manage_choice == "1":
            print("1. View users")
            print("2. Delete users")
            print("0. Done")
            admin_user_choice = input("Choose an option: ")
            if admin_user_choice == "1":
                view_all_users(session)            
            elif admin_user_choice == "2":
                delete_user(session)    
        elif admin_manage_choice == "2":
            print("1. View movies")
            print("2. Edit movies")
            print("3. Add new movies")
            print("4. Delete movies")
            print("0. Done")
            admin_movie_choice = input("Choose an option: ")
            if admin_movie_choice == "1":
                view_movies(user, session)
            elif admin_movie_choice == "2":
                edit_movies(session)
            elif admin_movie_choice == "3":
                add_new_movies(session)
            elif admin_movie_choice == "4":
                delete_movies(user, session)
    elif choice == "0":
        print("Goodbye!")
        sys.exit()
    profile_setting(user, session)


# Display user's movie lists
def display_movie_lists(user, session):
    user_profile = session.query(User).filter(User.username == user.username).first()
    watching_movies = user_profile.watching_list
    future_movies = user_profile.to_watch_list
    watched_movies = user_profile.watched_list
    # Functions to print the three lists; User's watching, to watch and watched lists
    print("\n-----------------------------------------------------------------------------")
    print("CURRENTLY WATCHING MOVIES")
    print("-----------------------------------------------------------------------------")
    # Print movies that are on the watching list.
    print_movies(watching_movies)

    # Print movies that are on the future list.
    print("\n-----------------------------------------------------------------------------")
    print("MOVIES TO WATCH IN THE FUTURE")
    print("-----------------------------------------------------------------------------")
    print_movies(future_movies)

    # Print movies that are on the watched list.
    print("\n-----------------------------------------------------------------------------")
    print("WATHCHED MOVIES")
    print("-----------------------------------------------------------------------------")
    print_movies(watched_movies)
    
    # Function to back to the profile setting
    profile_setting(user, session)

def print_movies(movie_list):
    # Print movies that are on the watching list.
    if not movie_list:
        print("No movies listed.")
    else:
        for movie in movie_list:
            print(f"id: {movie.id}, title: {movie.title}, genre: {movie.rating}, released: {movie.release_year}")
    

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
    print_movies(update_movie_from)
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
            if update_movie_to == user.watched_list:
                rate_mavies(movie)

# Function to let the users to rate movies they finish watching
def rate_mavies(movie):
    print("\n-----------------------------------------------------------------------------")
    print("RATE THIS MOVIE")
    print("-----------------------------------------------------------------------------")
    print("Enter a number between 1 and 5")
    print("1 for least and 5 for most favorite movie")
    user_rated_score = int(input("Choose an option: "))
    if user_rated_score in [1, 2, 3, 4, 5]:
        print("Your rating has been recorded.")


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
    print_movies(movie_list)
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

def view_all_users(session):
    all_users = session.query(User).all()
    for index, user in enumerate(all_users):
        print(f"{index + 1}. Username: {user.username}, Name: {user.name}, Email: {user.email}, role: {user.role}")


def delete_user(session):
    username = input("Username to remove: ")
    user_to_delete = session.query(User).filter(User.username == username).first()
    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()
    else:
        print(f"Username: {username} not found.")

def view_movies(user, session):
    get_best_movies(user, session)

# Function that allows admins to update movie from the movie database
def edit_movies(session):
    movie_title_to_update = input("Enter movie title: ")
    movie = session.query(Movie).filter(Movie.title == movie_title_to_update).first()    
    if movie:
        print("\n1. Change title")
        print("2. Edit description")
        print("3. Update rating")
        print("4. Change released year")
        print("0. Done")
        option = input("Choose an option: ")
        match option:
            case "1":
                title = input("New title: ")
                movie.title = title
                session.commit()
            case "2":
                description = input("Enter new description: ")
                movie.description = description
                session.commit()
            case "3":
                rating = float(input("Enter new rating: "))
                movie.rating = rating
                session.commit()
            case "4":
                released_year = int(input("Enter released_year: "))
                movie.release_year = released_year
                session.commit()
    else:
        print("Movie '{movie_title_to_update}' does not exist in the movie data.")
    
# Function that allows admins to add new movie to the movie database
def add_new_movies(session):
    title = input("Title: ")
    movie = session.query(Movie).filter(Movie.title == title).first()
    if not movie:
        description = input("Description: ")
        year = int(input("Released year: ") )
        new_movie = Movie(title=title, description=description, rating=0.0, release_year= year)
        session.add(new_movie)
        session.commit()
        print(f"Movie title '{title}' is added to the movie data.")
    else:
        print(f"Movie title '{title}' is already in the movie data.")
    

# Function that allows admin to delete a movie from the movie database with admin password 
def delete_movies(user, session):
    title = input("Enter movie title: ")
    movie = session.query(Movie).filter(Movie.title == title).first()
    if movie:
        password = getpass("Enter your password: ")
        if password == user.password:
            session.delete(movie)
            session.commit()
        else:
            print("Passwords do not match")

    else:
        print("Movie does not exist.")


        
        



