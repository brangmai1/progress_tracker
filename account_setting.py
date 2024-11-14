# user.py

import re
from tables import User
from getpass import getpass

ADMINS = ["brangmai@email.com"]

# Log-in function 
def log_in(session):
    username = input("Enter username: ").strip()
    user = session.query(User).filter(User.username == username).first()
    
    if not user:
        print(f"User '{username}' does not exist")
        return None
    
    password = getpass("Enter password: ").strip()
    if password != user.password:
        print("Incorrect password")
        return None
    
    print(f"\nWelcome back, {user.name.title()}!")
    return user

# Sign-up function 
def sign_up(session):
    new_username = set_username(session)    
    new_password = set_password() 
    new_name = input("Enter name: ")
    new_email = set_email(session)    
    new_user = User(username=new_username, password=new_password, name=new_name, email=new_email)
    if new_user.email in ADMINS:
        new_user.role = 'admin'
    session.add(new_user) 
    session.commit()
    return new_user

def settings(user, session):
    print("\nAccount settings")
    print("1. Change password")
    print("2. Change name")
    print("3. Change email")
    print("0. Done")
    choice = input("Chose an option: ")
    if choice == "1":
        change_password(user, session)
    elif choice == "2":
        change_name(user, session)
    elif choice == "3":
        change_email(user, session)

# Function to change the password of an existing user
def change_password(user, session):
    user.password = set_password()
    session.commit()
    print("Password changed")

# Function to change the name of an existing user
def change_name(user, session):
    user.name = input("Enter new name: ")
    session.commit()
    print("Name changed")

def change_email(user, session):
    user.email = set_email(session)
    session.commit()
    print("Email changed")

# Function to check Username 
def found_username(username, session):   
    user = session.query(User).filter(User.username == username).first()
    return user is not None

# Function to check Email
def found_email(email, session):
    email = session.query(User).filter(User.email == email).first()
    return email is not None

# Function to set a unique username
def set_username(session):
    while True:      
        new_username = input("Enter username: ")
        # Check a username format: a username must be a combination of letters and numbers only 
        # and starts with letters. The length of a username must be five and more.
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9]{4,}$", new_username):
            print("Invalid Username! Must be at least 5 characters.")
        # Check a new username is already existed in the database
        elif found_username(new_username, session):
            print("Username already taken. Choose another.")
        else:
            break
    return new_username

# Function to set a new password
def set_password():
    password = ""
    while True:
        if password == "":
            new_password = getpass("Enter new password: ")
        else:
            new_password = getpass("Confirm password: ")
        # Strong password pattern
        #pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if not re.match(r"^(?=.*[a-z])[a-zA-Z0-9@$!%*?&]{5,}$", new_password):
            print("Weak password! Use letters, numbers and special characters.")
        else:
            if password == "":
                password = new_password
            else:
                if password != new_password:
                    print("Passwords do not match")
                else:
                    break   
    return new_password

# Function to set a nique email
def set_email(session):
    while True:
        new_email = input("Enter email: ")
        # Check the user input email is the format of an email
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_.]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$", new_email):
            print("Invalid email format!")
        # Check the input email is alread used 
        elif found_email(new_email, session):
            print("Email already used.")
        else:
            break 
    return new_email





    