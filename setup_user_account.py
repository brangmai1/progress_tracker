from user import sign_up, log_in 
from search_movie import search
from tables import User

def setup_user(session):
    while True:
        print("1. Sign Up")
        print("2. Log In")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            print("Signing up...")
            user = sign_up(session)
            if user is not None:
                search(session)
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
    user_profile = session.query(User).filter(User.username == user).first()
    watching_movies = user_profile.watching_list
    future_movies = user_profile.to_watch_list
    watched_movies = user_profile.watched_list
    print("-----------------------------------------------------------------------------")
    print("CURRENTLY WATCHING MOVIES")
    print("-----------------------------------------------------------------------------")
    if not watching_movies:
        print("No movies currently watching.")
    else:
        for movie in watching_movies:
            print(f"id: {movie.id}, title: {movie.title}")
    print("-----------------------------------------------------------------------------")
    print("MOVIES TO WATCH IN THE FUTURE")
    print("-----------------------------------------------------------------------------")
    if not future_movies:
        print("No movies to watch in the future.")
    else:
        for movie in future_movies:
            print(f"id: {movie.id}, title: {movie.title}")
    print("-----------------------------------------------------------------------------")
    print("WATHCHED MOVIES")
    print("-----------------------------------------------------------------------------")
    if not watched_movies:
        print("No watched movies listed.")
    else:
        for movie in future_movies:
            print(f"id: {movie.id}, title: {movie.title}")

    search_movie = input("Do you want search Movies? Enter 'y' for 'Yes', 'n' for No: ")
    if search_movie.lower() == 'y':
        search(session)