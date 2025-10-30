import pandas as pd 
from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("the_movie_db_api_key")

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

for p in range(1, 5000):
    response = requests.get(url=f"https://api.themoviedb.org/3/discover/movie?page={p}", headers=headers)
    for movie in response.json()["results"]:
        movie_details = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie["id"]}", headers=headers).json()
        print(movie_details)
        try:
            movie_data = {"title": movie["title"], "date": pd.to_datetime(movie["release_date"]),
                      "popularity": movie["popularity"], "adult": movie["adult"],
                      "genre": movie_details["genres"][0]["name"], "budget": movie_details["budget"],
                      "revenue": movie_details["revenue"], "runtime": movie_details["runtime"]}
        except IndexError:
            continue
        
        movies.append(movie_data)

df = pd.DataFrame(movies)
df.to_csv("../datasets/test.csv")