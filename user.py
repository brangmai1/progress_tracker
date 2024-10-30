# user.py

import re
from tables import User

# Function to check Username 
def found_username(username, session):   
    user = session.query(User).filter(User.username == username).first()
    return user is not None

# Function to check Email
def found_email(email, session):
    email = session.query(User).filter(User.email == email).first()
    return email is not None

# Sign-up function 
def sign_up(session):
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
    while True:
        new_password = input("Enter your password: ")
        # Strong password pattern
        #pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if not re.match(r"^(?=.*[a-z])[a-zA-Z0-9@$!%*?&]{5,}$", new_password):
            print("Weak password! Use letters, numbers and special characters.")
        else:
            break        

    new_name = input("Enter your name: ")
    while True:
        new_email = input("Enter your email: ")
        # Check the user input email is the format of an email
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_.]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$", new_email):
            print("Invalid email format!")
        # Check the input email is alread used 
        elif found_email(new_email, session):
            print("Email already used.")
        else:
            break 
    new_user = User(username=new_username, password=new_password, name=new_name, email=new_email)
    session.add(new_user) 
    session.commit()
    return new_user


# Log-in function 
def log_in(session):
    username = input("Enter your username: ").strip()
    user = session.query(User).filter(User.username == username).first()
    
    if not user:
        print(f"User '{username}' does not exist")
        return None
    
    password = input("Enter your password: ").strip()
    if password != user.password:
        print("Incorrect password")
        return None
    
    print(f"Welcome back, {username}!")
    return user


if __name__ == "__main__":
    print()
    # while True:
    #     print("1. Sign Up")
    #     print("2. Log In")
    #     print("0. Exit")
    #     choice = input("Choose an option: ").strip()

    #     if choice == '1':
    #         sign_up()
    #     elif choice == '2':
    #         success = log_in()
    #         if success:
    #             break
    #     elif choice == '0':
    #         print("Goodbye!")
    #         break
    #     else:
    #         print("Invalid option. Try again.")

# Base = declarative_base()

# # Relationship table between users table and movies table, many-to-many relationship
# class UserMovieToWatch(Base):
#     __tablename__ = "user_movie_to_watch"  
#     id = Column(Integer, primary_key=True)  
#     username = Column(String(25), ForeignKey("users.username", ondelete="CASCADE"))
#     movie_id = Column(Integer, ForeignKey("movies.id", ondelete="CASCADE"))


# # # Relationship table between users table and movies table, many-to-many relationship
# class UserMovieWatching(Base):
#     __tablename__ = "user_movie_watching"
#     id = Column(Integer, primary_key=True)
#     username = Column(String(25), ForeignKey("users.username", ondelete="CASCADE"))
#     movie_id = Column(Integer, ForeignKey("movies.id", ondelete="CASCADE"))


# # # Relationship table between users table and movies table, many-to-many relationship
# class UserMovieWatched(Base):    
#     __tablename__ = "user_movie_watched"
#     id = Column(Integer, primary_key=True)
#     username = Column(String(25), ForeignKey("users.username", ondelete="CASCADE"))
#     movie_id = Column(Integer, ForeignKey("movies.id", ondelete="CASCADE"))


# # User class
# class User(Base):
#     __tablename__ = "users"
#     username = Column(String (15), primary_key=True)
#     password = Column(String (25), nullable=False)
#     name = Column(String (25), nullable=False)
#     email = Column(String (25), nullable=True)
#     to_watch_list = relationship("Movie", secondary="user_movie_to_watch", back_populates="future_list")
#     watching_list = relationship("Movie", secondary="user_movie_watching", back_populates="current_list")
#     watched_list = relationship("Movie", secondary="user_movie_watched", back_populates="watched_list")
