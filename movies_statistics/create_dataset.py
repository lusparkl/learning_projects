import pandas as pd 
import requests


response = requests.get(url=f"https://api.imdbapi.dev/titles?types=MOVIE")
page_token = response.json()["nextPageToken"]

movies = []

for p in range(1, 5000):
    response = requests.get(url=f"https://api.imdbapi.dev/titles?types=MOVIE&pageToken={page_token}")
    data = response.json()
    page_token = data["nextPageToken"]
    for movie in data["titles"]:
        print(movie)
        try:
            movie_data = {"title": movie["primaryTitle"], "year": pd.to_datetime(movie["startYear"]),
                      "rating": movie["rating"]["aggregateRating"], 
                      "genre": movie["genres"][0], "runtime": movie["runtimeSeconds"]}
        except (IndexError, KeyError):
            continue
        
        movies.append(movie_data)

df = pd.DataFrame(movies)
df.to_csv("../datasets/movies.csv")