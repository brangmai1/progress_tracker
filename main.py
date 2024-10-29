from initial_setup import setup_table_data
from setup_user_account import setup_user
from connect_database import make_session

def main():
    print("----------------------------------------------")
    print("MOVIE BINGE-WATCHING PROGRESS TRACKER PROJECT")
    print("----------------------------------------------")
    # Function to setup initial tables and populate data
    with make_session() as session:
        setup_table_data(session)
        setup_user(session)

if __name__ == "__main__":    
    main()
   
    

            
