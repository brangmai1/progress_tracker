from sqlalchemy import Table, ForeignKey, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, relationship
from connect_database import get_engine, make_session, close_session
import pandas as pd


# Define a base class and models
Base = declarative_base()

# Association table for many-to-many relationship between Movie and Genre
movie_genre_association = Table(
    "movie_genre", Base.metadata,
    Column("movie_id", Integer, ForeignKey("movies.id", ondelete="CASCADE"), primary_key=True),
    Column("genre_id", Integer, ForeignKey("genres.id", ondelete="CASCADE"), primary_key=True)
)

# # Movie model
class Movie(Base):
    __tablename__ = "movies" # table name = movies
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(1000))
    rating = Column(Float)
    release_year = Column(Integer)
    # Relationship with Genre through the association table
    genres = relationship("Genre", secondary=movie_genre_association, back_populates="movies")

    def __repr__(self):
        return f"movie_id: {self.id}, title: \"{self.title}\", rating: {self.rating}, release year: {self.release_year}"


# Genre Model   
class Genre(Base):
    __tablename__ = "genres" # table name = genres
    id = Column(Integer, primary_key=True)
    genre_type = Column(String(50), unique=True, nullable=False)
    # Relationship with Movie through the association table
    movies = relationship("Movie", secondary=movie_genre_association, back_populates="genres")

    def __repr__(self):
        return f"genre_id: {self.id}, genre_type: {self.genre_type}"


def get_genres_list(filename):
    genres = []
    with open(filename, "r") as file:
        lines = file.readlines()        
        for item in lines:
            genres.append(item.strip())
    return genres

def insert_into_genres(csv_file, session):
    genres_list = get_genres_list(csv_file)
    for i in range(len(genres_list)):
        session.add(Genre(id=i+1, genre_type=genres_list[i]))
    session.commit()

def insert_into_movies(movie_data, session):
    movies_df = pd.read_csv(movie_data)
    for _, row in movies_df.iterrows():
        session.add(Movie(id=int(row.iloc[0]+1), title=row.iloc[1], description=row.iloc[2], rating=float(row.iloc[3]), release_year=int(row.iloc[4])))
    session.commit()

def select_from_genre(session):
    print("SELECT * FROM genres.........")
    genres = session.query(Genre).all()
    for genre in genres:
        print(genre)

def select_from_movies(session):
    print("SELECT * FROM movies......")
    movies = session.query(Movie).all()
    for movie in movies:
        print(movie)

def associate_movie_genre(session):
    action = session.query(Genre).filter(Genre.genre_type == "Action").first()
    adventure = session.query(Genre).filter(Genre.genre_type == "Adventure").first()
    animation = session.query(Genre).filter(Genre.genre_type == "Animation").first()
    biography = session.query(Genre).filter(Genre.genre_type == "Biography").first()
    comedy = session.query(Genre).filter(Genre.genre_type == "Comedy").first()
    crime = session.query(Genre).filter(Genre.genre_type == "Crime").first()
    drama = session.query(Genre).filter(Genre.genre_type == "Drama").first()
    family = session.query(Genre).filter(Genre.genre_type == "Family").first()
    fantasy = session.query(Genre).filter(Genre.genre_type == "Fantasy").first()
    film_noir = session.query(Genre).filter(Genre.genre_type == "Film-Noir").first()
    history = session.query(Genre).filter(Genre.genre_type == "History").first()
    horror = session.query(Genre).filter(Genre.genre_type == "Horror").first()
    music = session.query(Genre).filter(Genre.genre_type == "Music").first()
    musical = session.query(Genre).filter(Genre.genre_type == "Musical").first()
    mystery = session.query(Genre).filter(Genre.genre_type == "Mystery").first()
    romance = session.query(Genre).filter(Genre.genre_type == "Romance").first()
    sci_fi = session.query(Genre).filter(Genre.genre_type == "Sci-Fi").first()
    thriller = session.query(Genre).filter(Genre.genre_type == "Thriller").first()
    war = session.query(Genre).filter(Genre.genre_type == "War").first()
    western = session.query(Genre).filter(Genre.genre_type == "Western").first()

    movie_id_1 = session.query(Movie).filter(Movie.id == 1).first()
    movie_id_2 = session.query(Movie).filter(Movie.id == 2).first()
    movie_id_3 = session.query(Movie).filter(Movie.id == 3).first()
    movie_id_4 = session.query(Movie).filter(Movie.id == 4).first()
    movie_id_5 = session.query(Movie).filter(Movie.id == 5).first()
    movie_id_6 = session.query(Movie).filter(Movie.id == 6).first()
    movie_id_7 = session.query(Movie).filter(Movie.id == 7).first()
    movie_id_8 = session.query(Movie).filter(Movie.id == 8).first()
    movie_id_9 = session.query(Movie).filter(Movie.id == 9).first()
    movie_id_10 = session.query(Movie).filter(Movie.id == 10).first()

    movie_id_11 = session.query(Movie).filter(Movie.id == 11).first()
    movie_id_12 = session.query(Movie).filter(Movie.id == 12).first()
    movie_id_13 = session.query(Movie).filter(Movie.id == 13).first()
    movie_id_14 = session.query(Movie).filter(Movie.id == 14).first()
    movie_id_15 = session.query(Movie).filter(Movie.id == 15).first()
    movie_id_16 = session.query(Movie).filter(Movie.id == 16).first()
    movie_id_17 = session.query(Movie).filter(Movie.id == 17).first()
    movie_id_18 = session.query(Movie).filter(Movie.id == 18).first()
    movie_id_19 = session.query(Movie).filter(Movie.id == 19).first()
    movie_id_20 = session.query(Movie).filter(Movie.id == 20).first()

    movie_id_21 = session.query(Movie).filter(Movie.id == 21).first()
    movie_id_22 = session.query(Movie).filter(Movie.id == 22).first()
    movie_id_23 = session.query(Movie).filter(Movie.id == 23).first()
    movie_id_24 = session.query(Movie).filter(Movie.id == 24).first()
    movie_id_25 = session.query(Movie).filter(Movie.id == 25).first()
    movie_id_26 = session.query(Movie).filter(Movie.id == 26).first()
    movie_id_27 = session.query(Movie).filter(Movie.id == 27).first()
    movie_id_28 = session.query(Movie).filter(Movie.id == 28).first()
    movie_id_29 = session.query(Movie).filter(Movie.id == 29).first()
    movie_id_30 = session.query(Movie).filter(Movie.id == 30).first()

    movie_id_31 = session.query(Movie).filter(Movie.id == 31).first()
    movie_id_32 = session.query(Movie).filter(Movie.id == 32).first()
    movie_id_33 = session.query(Movie).filter(Movie.id == 33).first()
    movie_id_34 = session.query(Movie).filter(Movie.id == 34).first()
    movie_id_35 = session.query(Movie).filter(Movie.id == 35).first()
    movie_id_36 = session.query(Movie).filter(Movie.id == 36).first()
    movie_id_37 = session.query(Movie).filter(Movie.id == 37).first()
    movie_id_38 = session.query(Movie).filter(Movie.id == 38).first()
    movie_id_39 = session.query(Movie).filter(Movie.id == 39).first()
    movie_id_40 = session.query(Movie).filter(Movie.id == 40).first()

    movie_id_41 = session.query(Movie).filter(Movie.id == 41).first()
    movie_id_42 = session.query(Movie).filter(Movie.id == 42).first()
    movie_id_43 = session.query(Movie).filter(Movie.id == 43).first()
    movie_id_44 = session.query(Movie).filter(Movie.id == 44).first()
    movie_id_45 = session.query(Movie).filter(Movie.id == 45).first()
    movie_id_46 = session.query(Movie).filter(Movie.id == 46).first()
    movie_id_47 = session.query(Movie).filter(Movie.id == 47).first()
    movie_id_48 = session.query(Movie).filter(Movie.id == 48).first()
    movie_id_49 = session.query(Movie).filter(Movie.id == 49).first()
    movie_id_50 = session.query(Movie).filter(Movie.id == 50).first()

    movie_id_51 = session.query(Movie).filter(Movie.id == 51).first()
    movie_id_52 = session.query(Movie).filter(Movie.id == 52).first()
    movie_id_53 = session.query(Movie).filter(Movie.id == 53).first()
    movie_id_54 = session.query(Movie).filter(Movie.id == 54).first()
    movie_id_55 = session.query(Movie).filter(Movie.id == 55).first()
    movie_id_56 = session.query(Movie).filter(Movie.id == 56).first()
    movie_id_57 = session.query(Movie).filter(Movie.id == 57).first()
    movie_id_58 = session.query(Movie).filter(Movie.id == 58).first()
    movie_id_59 = session.query(Movie).filter(Movie.id == 59).first()
    movie_id_60 = session.query(Movie).filter(Movie.id == 60).first()

    movie_id_61 = session.query(Movie).filter(Movie.id == 61).first()
    movie_id_62 = session.query(Movie).filter(Movie.id == 62).first()
    movie_id_63 = session.query(Movie).filter(Movie.id == 63).first()
    movie_id_64 = session.query(Movie).filter(Movie.id == 64).first()
    movie_id_65 = session.query(Movie).filter(Movie.id == 65).first()
    movie_id_66 = session.query(Movie).filter(Movie.id == 66).first()
    movie_id_67 = session.query(Movie).filter(Movie.id == 67).first()
    movie_id_68 = session.query(Movie).filter(Movie.id == 68).first()
    movie_id_69 = session.query(Movie).filter(Movie.id == 69).first()
    movie_id_70 = session.query(Movie).filter(Movie.id == 70).first()

    movie_id_71 = session.query(Movie).filter(Movie.id == 71).first()
    movie_id_72 = session.query(Movie).filter(Movie.id == 72).first()
    movie_id_73 = session.query(Movie).filter(Movie.id == 73).first()
    movie_id_74 = session.query(Movie).filter(Movie.id == 74).first()
    movie_id_75 = session.query(Movie).filter(Movie.id == 75).first()
    movie_id_76 = session.query(Movie).filter(Movie.id == 76).first()
    movie_id_77 = session.query(Movie).filter(Movie.id == 77).first()
    movie_id_78 = session.query(Movie).filter(Movie.id == 78).first()
    movie_id_79 = session.query(Movie).filter(Movie.id == 79).first()
    movie_id_80 = session.query(Movie).filter(Movie.id == 80).first()

    movie_id_81 = session.query(Movie).filter(Movie.id == 81).first()
    movie_id_82 = session.query(Movie).filter(Movie.id == 82).first()
    movie_id_83 = session.query(Movie).filter(Movie.id == 83).first()
    movie_id_84 = session.query(Movie).filter(Movie.id == 84).first()
    movie_id_85 = session.query(Movie).filter(Movie.id == 85).first()
    movie_id_86 = session.query(Movie).filter(Movie.id == 86).first()
    movie_id_87 = session.query(Movie).filter(Movie.id == 87).first()
    movie_id_88 = session.query(Movie).filter(Movie.id == 88).first()
    movie_id_89 = session.query(Movie).filter(Movie.id == 89).first()
    movie_id_90 = session.query(Movie).filter(Movie.id == 90).first()

    movie_id_91 = session.query(Movie).filter(Movie.id == 91).first()
    movie_id_92 = session.query(Movie).filter(Movie.id == 92).first()
    movie_id_93 = session.query(Movie).filter(Movie.id == 93).first()
    movie_id_94 = session.query(Movie).filter(Movie.id == 94).first()
    movie_id_95 = session.query(Movie).filter(Movie.id == 95).first()
    movie_id_96 = session.query(Movie).filter(Movie.id == 96).first()
    movie_id_97 = session.query(Movie).filter(Movie.id == 97).first()
    movie_id_98 = session.query(Movie).filter(Movie.id == 98).first()
    movie_id_99 = session.query(Movie).filter(Movie.id == 99).first()
    movie_id_100 = session.query(Movie).filter(Movie.id == 100).first()

    movie_id_1.genres.extend([drama])
    movie_id_2.genres.extend([crime, drama])
    movie_id_3.genres.extend([action, crime, drama])
    movie_id_4.genres.extend([action, adventure, drama])
    movie_id_5.genres.extend([biography, drama, history])
    movie_id_6.genres.extend([crime, drama])
    movie_id_7.genres.extend([crime, drama])
    movie_id_8.genres.extend([crime, drama])
    movie_id_9.genres.extend([drama])
    movie_id_10.genres.extend([drama, romance])

    movie_id_11.genres.extend([action, adventure, drama])
    movie_id_12.genres.extend([adventure, western])
    movie_id_13.genres.extend([action, adventure, drama])
    movie_id_14.genres.extend([adventure, drama, sci_fi])
    movie_id_15.genres.extend([animation, action, adventure])
    movie_id_16.genres.extend([action, adventure, sci_fi])
    movie_id_17.genres.extend([action, adventure, fantasy])
    movie_id_18.genres.extend([action, sci_fi])
    movie_id_19.genres.extend([biography, crime, drama])
    movie_id_20.genres.extend([biography, drama, history])

    movie_id_21.genres.extend([comedy, drama, romance])
    movie_id_22.genres.extend([drama, war])
    movie_id_23.genres.extend([crime, drama, mystery])
    movie_id_24.genres.extend([action, sci_fi])
    movie_id_25.genres.extend([crime, drama])
    movie_id_26.genres.extend([crime, drama, fantasy])
    movie_id_27.genres.extend([animation, adventure, family])
    movie_id_28.genres.extend([action, drama, mystery])
    movie_id_29.genres.extend([crime, drama, thriller])
    movie_id_30.genres.extend([action, adventure, fantasy])

    movie_id_31.genres.extend([action, drama])
    movie_id_32.genres.extend([drama, family, fantasy])
    movie_id_33.genres.extend([drama])
    movie_id_34.genres.extend([biography, comedy, drama])
    movie_id_35.genres.extend([drama, western])
    movie_id_36.genres.extend([drama, mystery, sci_fi])
    movie_id_37.genres.extend([horror, mystery, thriller])
    movie_id_38.genres.extend([drama, romance, war])
    movie_id_39.genres.extend([comedy, drama, romance])
    movie_id_40.genres.extend([horror, sci_fi])

    movie_id_41.genres.extend([mystery, thriller])
    movie_id_42.genres.extend([drama, music])
    movie_id_43.genres.extend([comedy, drama, romance])
    movie_id_44.genres.extend([western])
    movie_id_45.genres.extend([adventure, comedy, sci_fi])
    movie_id_46.genres.extend([action, adventure, drama])
    movie_id_47.genres.extend([drama, romance])
    movie_id_48.genres.extend([animation])
    movie_id_49.genres.extend([action, crime, drama])
    movie_id_50.genres.extend([animation, adventure, drama])

    movie_id_51.genres.extend([crime, drama, mystery])
    movie_id_52.genres.extend([crime, drama, thriller])
    movie_id_53.genres.extend([drama, thriller])
    movie_id_54.genres.extend([crime, drama])
    movie_id_55.genres.extend([biography, drama, music])
    movie_id_56.genres.extend([action, adventure, drama])
    movie_id_57.genres.extend([crime, drama, thriller])
    movie_id_58.genres.extend([animation, adventure, family])
    movie_id_59.genres.extend([action, drama, mystery])
    movie_id_60.genres.extend([mystery, thriller])

    movie_id_61.genres.extend([animation, adventure, comedy])
    movie_id_62.genres.extend([animation, drama, fantasy])
    movie_id_63.genres.extend([action, adventure, sci_fi])
    movie_id_64.genres.extend([action, drama])
    movie_id_65.genres.extend([comedy, drama])
    movie_id_66.genres.extend([adventure, drama, war])
    movie_id_67.genres.extend([animation, action, adventure])
    movie_id_68.genres.extend([drama])
    movie_id_69.genres.extend([crime, drama, mystery])
    movie_id_70.genres.extend([drama, war])

    movie_id_71.genres.extend([biography, drama, music])
    movie_id_72.genres.extend([drama, war])
    movie_id_73.genres.extend([drama, mystery, thriller])
    movie_id_74.genres.extend([comedy, drama, war])
    movie_id_75.genres.extend([comedy, war])
    movie_id_76.genres.extend([drama, film_noir])
    movie_id_77.genres.extend([drama, thriller, war])
    movie_id_78.genres.extend([action, adventure, sci_fi])
    movie_id_79.genres.extend([drama, horror])
    movie_id_80.genres.extend([crime, drama, mystery])

    movie_id_81.genres.extend([action, adventure])
    movie_id_82.genres.extend([drama, mystery, war])
    movie_id_83.genres.extend([drama])
    movie_id_84.genres.extend([animation, adventure, comedy])
    movie_id_85.genres.extend([drama])
    movie_id_86.genres.extend([drama, romance, sci_fi])
    movie_id_87.genres.extend([crime, thriller])
    movie_id_88.genres.extend([drama])
    movie_id_89.genres.extend([drama, romance])
    movie_id_90.genres.extend([animation, action, adventure])

    movie_id_91.genres.extend([biography, drama, history])
    movie_id_92.genres.extend([animation, adventure, comedy])
    movie_id_93.genres.extend([action, adventure, fantasy])
    movie_id_94.genres.extend([crime, drama])
    movie_id_95.genres.extend([adventure, biography, drama])
    movie_id_96.genres.extend([adventure, sci_fi])
    movie_id_97.genres.extend([comedy, musical, romance])
    movie_id_98.genres.extend([drama])
    movie_id_99.genres.extend([drama, mystery])
    movie_id_100.genres.extend([crime, mystery, thriller]) 

    session.commit()   
   

# Create all tables  
engine = get_engine() 
Base.metadata.create_all(engine)
# Create a session to interact with the database
session = make_session(engine)

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
associate_movie_genre(session)

close_session(session)


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


