from sqlalchemy import String, Integer, Column, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship
from connect_database import get_engine

Base = declarative_base()

# Association table for many-to-many relationship between Movie and Genre
class MovieGenreAssociation(Base):
    __tablename__ = "movie_genre"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movies.id", ondelete="CASCADE"))
    genre_id = Column(Integer, ForeignKey("genres.id", ondelete="CASCADE"))

# Relationship table between users table and movies table, many-to-many relationship
class UserMovieToWatch(Base):
    __tablename__ = "user_movie_to_watch"  
    id = Column(Integer, primary_key=True)  
    username = Column(String(25), ForeignKey("users.username", ondelete="CASCADE"))
    movie_id = Column(Integer, ForeignKey("movies.id", ondelete="CASCADE"))


# # Relationship table between users table and movies table, many-to-many relationship
class UserMovieWatching(Base):
    __tablename__ = "user_movie_watching"
    id = Column(Integer, primary_key=True)
    username = Column(String(25), ForeignKey("users.username", ondelete="CASCADE"))
    movie_id = Column(Integer, ForeignKey("movies.id", ondelete="CASCADE"))


# # Relationship table between users table and movies table, many-to-many relationship
class UserMovieWatched(Base):    
    __tablename__ = "user_movie_watched"
    id = Column(Integer, primary_key=True)
    username = Column(String(25), ForeignKey("users.username", ondelete="CASCADE"))
    movie_id = Column(Integer, ForeignKey("movies.id", ondelete="CASCADE"))


# # Movie model
class Movie(Base):
    __tablename__ = "movies" # table name = movies
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(1000))
    rating = Column(Float)
    release_year = Column(Integer)
    # Relationship with Genre through the association table
    genres = relationship("Genre", secondary="movie_genre", back_populates="movies")
    current_list = relationship("User", secondary="user_movie_watching", back_populates="watching_list")
    future_list = relationship("User", secondary="user_movie_to_watch", back_populates="to_watch_list")
    watched_list = relationship("User", secondary="user_movie_watched", back_populates="watched_list")

    def __repr__(self):
        return f"movie_id: {self.id}, title: \"{self.title}\", rating: {self.rating}, release year: {self.release_year}"
    
# Genre Model   
class Genre(Base):
    __tablename__ = "genres" # table name = genres
    id = Column(Integer, primary_key=True)
    genre_type = Column(String(50), unique=True, nullable=False)
    # Relationship with Movie through the association table
    movies = relationship("Movie", secondary="movie_genre", back_populates="genres")

    def __repr__(self):
        return f"genre_id: {self.id}, genre_type: {self.genre_type}"

# User class
class User(Base):
    __tablename__ = "users"
    username = Column(String (50), primary_key=True)
    password = Column(String (256), nullable=False)
    name = Column(String (50), nullable=False)
    email = Column(String (254), nullable=True)
    role = Column(String(10), default="user")
    watching_list = relationship("Movie", secondary="user_movie_watching", back_populates="current_list")
    to_watch_list = relationship("Movie", secondary="user_movie_to_watch", back_populates="future_list")
    watched_list = relationship("Movie", secondary="user_movie_watched", back_populates="watched_list")

def set_tables(session):
    engine = get_engine()
    Base.metadata.create_all(engine)
    session.commit()
    
   