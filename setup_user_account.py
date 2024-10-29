from user import sign_up, log_in 
from search_movie import search

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
                search(session)
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")