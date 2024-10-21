import pandas as pd

genre_raw = "genre.csv"
def get_genres(filename):
    genres = []
    with open(filename, "r") as file:
        lines = file.readlines()        
        for item in lines:
            genres.append(item.strip())
    return genres

# genres = get_genres(genre_raw)
# for item in genres:
#     print(item)

movie_df = pd.read_csv("top_movies.csv")
for index, row in movie_df.iterrows():
    id = row.iloc[0]
    title = row.iloc[1]
    des = row.iloc[2]
    rating = row.iloc[3]
    year = row.iloc[4]

    print(id, title, des, rating, year)

       