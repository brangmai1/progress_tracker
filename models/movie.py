# from sqlalchemy import Column, Integer, String, Float
# from sqlalchemy.orm import declarative_base, relationship
# from connect_database import get_engine, make_session, close_session
# from movie_genre import movie_genre_association
# import pandas as pd

# # Define a base class and models
# Base = declarative_base()

# # # Movie model
# class Movie(Base):
#     __tablename__ = "movies" # table name = movies
#     id = Column(Integer, primary_key=True)
#     title = Column(String(100), nullable=False)
#     description = Column(String(1000))
#     rating = Column(Float)
#     release_year = Column(Integer)
#     # Relationship with Genre through the association table
#     genres = relationship("Genre", secondary="movie_genre", back_populates="movies")
#     future_list = relationship("User", secondary="user_movie_to_watch", back_populates="to_watch_list")
#     current_list = relationship("User", secondary="user_movie_watching", back_populates="watching_list")
#     watched_list = relationship("User", secondary="user_movie_watched", back_populates="watched_list")

#     def __repr__(self):
#         return f"movie_id: {self.id}, title: \"{self.title}\", rating: {self.rating}, release year: {self.release_year}"


# def insert_into_movies(movie_data, session):
#     movies_df = pd.read_csv(movie_data)
#     for _, row in movies_df.iterrows():
#         session.add(Movie(id=int(row.iloc[0]+1), title=row.iloc[1], description=row.iloc[2], rating=float(row.iloc[3]), release_year=int(row.iloc[4])))
#     session.commit()

# def select_from_movies(session):
#     print("SELECT * FROM movies......")
#     movies = session.query(Movie).all()
#     for movie in movies:
#         print(movie)

   
# if __name__ == "__main__":
#     print()
#     # Create all tables  
#     # engine = get_engine() 
#     # Base.metadata.create_all(engine)
#     # # Create a session to interact with the database
#     session = make_session()
#     select_from_movies(session)
#     close_session(session)

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
