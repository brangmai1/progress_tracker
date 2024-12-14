from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

database_url = "mysql+mysqlconnector://<username>:<password>@localhost/movie_progress_tracker"

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

# def make_session():
#     engine = create_engine(database_url)
#     # engine = get_engine()
#     session = sessionmaker(bind=engine)    
#     try:
#         yield session
#         session.commit() # Commit changes
#     except Exception as e:
#         session.rollback() # Rollback on error
#         raise e
#     finally:
#         session.close()

