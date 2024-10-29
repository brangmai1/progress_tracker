# models/genre.py

# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import declarative_base, relationship
# from models.connect_database import get_engine, make_session, close_session
# import pandas as pd


# # Define a base class and models
# Base = declarative_base()

# # Genre Model   
# class Genre(Base):
#     __tablename__ = "genres" # table name = genres
#     id = Column(Integer, primary_key=True)
#     genre_type = Column(String(50), unique=True, nullable=False)
#     # Relationship with Movie through the association table
#     movies = relationship("Movie", secondary="movie_genre", back_populates="genres")

#     def __repr__(self):
#         return f"genre_id: {self.id}, genre_type: {self.genre_type}"


# def get_genres_list(filename):
#     genres = []
#     with open(filename, "r") as file:
#         lines = file.readlines()        
#         for item in lines:
#             genres.append(item.strip())
#     return genres

# def insert_into_genres(csv_file, session):
#     genres_list = get_genres_list(csv_file)
#     for i in range(len(genres_list)):
#         session.add(Genre(id=i+1, genre_type=genres_list[i]))
#     session.commit()

# def select_from_genre(session):
#     print("SELECT * FROM genres.........")
#     genres = session.query(Genre).all()
#     for genre in genres:
#         print(genre)
   
# if __name__ == "__main__":
#     print()
    # Create all tables  
    # engine = get_engine() 
    # Base.metadata.create_all(engine)
    # # Create a session to interact with the database
    # session = make_session(engine)
    # close_session(session)

# Insert genres data in ORM table
# csv_file = "genre.csv"
# insert_into_genres(csv_file, session)
#select_from_genre(session)

# Insert movies data into ORM table
# movie_data = "top_movies.csv"
# insert_into_movies(movie_data, session)

# Query from movies table
# select_from_movies(session)

# Insert data into movie_genre table
# associate_movie_genre(session)




# action = Genre(id=1, genre_type = "Action")
# scifi = Genre(id=2, genre_type="Sci-Fi")

# # Insert Data into the database
# new_movie = Movie(id=1, title="The Lord of the Ring", description="The best movie of all time", rating=9.9, release=2003, genres=[action, scifi])
# session.add(new_movie)
# session.commit()

# new_genre = Genre(id=1, genre_type="Action")
# session.add(new_genre)
# session.commit()

# Query data from the database
# Get all movies 
# movies = session.query(Movie).all()
# print("Top movies.....")
# for movie in movies:
#     print(movie)

# Filter movies by rating
# high_rated = session.query(Movie).filter(Movie.rating > 9.0).all()
# print("Highly rated movies.....")
# print(high_rated)

# Update/modify Data
# movie = session.query(Movie).filter_by(title="The Lord of the Ring").first()
# movie.rating = 10
# session.commit()

# Movies after modification
# best_movies = session.query(Movie).all()
# for movie in best_movies:
#     print(movie)

# Delete data
# movie_delete = session.query(Movie).filter_by(title="The Lord of the Ring").first()
# session.delete(movie)
# session.commit()

# Movies after modification
# best_movies = session.query(Movie).all()
# for movie in best_movies:
#     print(movie)

# genre = session.query(Genre).all()
# for gen in genre:
#     print(gen)


