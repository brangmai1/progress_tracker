from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv
import os

load_dotenv()

# Check if Render provides a DATABAE_URL
database_url = os.getenv("DATABASE_URL")

if not database_url:
    # Fallback to individual environment variables
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "3306")

    database_url = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

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



if __name__=="__main__":
    print("DB_NAME:", os.getenv("DB_NAME"))
    print("DB_USER:", os.getenv("DB_USER"))
    print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
    print("DB_HOST:", os.getenv("DB_HOST"))
    print("DB_PORT:", os.getenv("DB_PORT"))