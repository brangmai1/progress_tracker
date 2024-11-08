from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError


database_url = "mysql+mysqlconnector://root:a3n5D4ng1@localhost/progress_tracker"

# Function to connect to database 
def get_engine():
    # Create an engine and connect to MySQ
    engine = create_engine(database_url)
    try:
        with engine.connect() as connection:
            print("Connected to the database.")
    except OperationalError as e:
        print(f"Connection failed: {e}")
        return None
    return engine

# Function returns session 
def make_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()

# Function to close session if it is open 
def close_session(session):
    if session.is_active:
        session.close()
    else:
        print("Session is inactive or closed.")