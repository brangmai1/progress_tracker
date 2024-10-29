from user import sign_up, log_in
from connect_database import get_engine
from sqlalchemy.orm import sessionmaker
from tables import set_tables
from insert_data import set_data
   
# Function to setup initial tables and populate data
def setup_tables_data():
    print()
     # set_tables()
    # set_data()

def setup_user():
    while True:
        print("1. Sign Up")
        print("2. Log In")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            print("Signing up...")
            sign_up()
        elif choice == '2':
            success = log_in()
            if success:
                break
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
def main():
    print("----------------------------------------------")
    print("MOVIE BINGE-WATCHING PROGRESS TRACKER PROJECT")
    print("----------------------------------------------")
    setup_tables_data()
    setup_user()

if __name__ == "__main__":
    
    main()
   
    

            
