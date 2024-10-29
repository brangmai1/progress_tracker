
from initial_setup import setup_table_data
from setup_user_account import setup_user

# def setup_user():
#     while True:
#         print("1. Sign Up")
#         print("2. Log In")
#         print("0. Exit")
#         choice = input("Choose an option: ").strip()

#         if choice == '1':
#             print("Signing up...")
#             sign_up()
#         elif choice == '2':
#             success = log_in()
#             if success:
#                 break
#         elif choice == '0':
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid option. Try again.")
def main():
    print("----------------------------------------------")
    print("MOVIE BINGE-WATCHING PROGRESS TRACKER PROJECT")
    print("----------------------------------------------")
    # Function to setup initial tables and populate data
    setup_table_data()
    setup_user()

if __name__ == "__main__":    
    main()
   
    

            
