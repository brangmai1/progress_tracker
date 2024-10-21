
from sqlalchemy import Table, Column, ForeignKey, String, Integer
from sqlalchemy.orm import declarative_base, relationship
from connect_database import get_engine, make_session, close_session
import re

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    username = Column(String (15), primary_key=True)
    password = Column(String (25), nullable=False)
    name = Column(String (25), nullable=False)
    email = Column(String (25), nullable=True)
    
    
def sign_up(session):
    while True:      
        new_username = input("Enter username: ")
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9]{4,}$", new_username):
            print("Ivalid Username!")
            print("Please try another username with letters and numers with a minimum length of 5.")
        else:
            break
    while True:
        new_password = input("Enter your password: ")
        # Strong password pattern
        #pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if not re.match(r"^(?=.*[a-z])[a-zA-Z0-9@$!%*?&]{5,}$", new_password):
            print("The password you entered is weak!")
            print("Please, enter a combination of letters, numbers and special characters for a strong password.")
        else:
            break        

    new_name = input("Enter your name: ")
    while True:
        new_email = input("Enter your email: ")
        if not re.match(r"^[a-zA-Z][a-zA-Z0-9_.]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$", new_email):
            print("Invalid email!")
        else:
            break 
    new_user = User(username=new_username, password=new_password, name=new_name, email=new_email)
    session.add(new_user) 
    session.commit()


if __name__ == "__main__":
    engine = get_engine()
    Base.metadata.create_all(engine)
    session = make_session(engine)
    sign_up(session)
    close_session(session)