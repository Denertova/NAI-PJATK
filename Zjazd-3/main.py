"""
Silnik rekomendacji filmów - Movie Recommendation Engine
Autor: Klaudia Denert s29276
Opis:
    Ten skrypt implementuje silnik rekomendacji filmów i seriali przy użyciu filtracji współrzędnych (collaborative filtering).
    Na podstawie ocen użytkowników w pliku JSON sugeruje 5 filmów, które użytkownik może polubić (rekomendacje)
    oraz 5 filmów, których użytkownik powinien unikać (anty-rekomendacje).
    Dodatkowe informacje o filmach pobierane są z OMDb API (https://www.omdbapi.com/).

Instrukcja użycia:
    1. Uzyskaj klucz API OMDb pod adresem https://www.omdbapi.com/apikey.aspx
    2. Uruchom skrypt i podaj nazwę użytkownika (dokładne komendy w pliku README w repozytorium).
"""

import json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import requests

JSON_FILE = "data/user_ratings.json"
OMDB_API_KEY = "place_your_omdb_api_key_here"

def load_data(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    records = []
    for user in data:
        for rating in user["ratings"]:
            records.append({"user": user["name"], "title": rating["title"], "score": rating["score"]})
    df = pd.DataFrame(records)
    return df

def build_user_item_matrix(df):
    return df.pivot_table(index='user', columns='title', values='score')

def get_similar_users(user_matrix, target_user):
    similarity = cosine_similarity(user_matrix.fillna(0))
    sim_df = pd.DataFrame(similarity, index=user_matrix.index, columns=user_matrix.index)
    return sim_df[target_user].drop(target_user).sort_values(ascending=False)

def recommend_movies(user_matrix, target_user, top_n=5):
    similar_users = get_similar_users(user_matrix, target_user)
    user_ratings = user_matrix.loc[target_user]
    
    weighted_scores = pd.Series(dtype=float)
    for other_user, sim_score in similar_users.items():
        other_ratings = user_matrix.loc[other_user]
        weighted_scores = weighted_scores.add(other_ratings * sim_score, fill_value=0)
    
    unrated_movies = user_ratings[user_ratings.isna()].index
    weighted_scores = weighted_scores[unrated_movies]
    top_movies = weighted_scores.sort_values(ascending=False).head(top_n)
    bottom_movies = weighted_scores.sort_values(ascending=True).head(top_n)
    return top_movies.index.tolist(), bottom_movies.index.tolist()

def fetch_movie_info(title, api_key):
    url = f"https://www.omdbapi.com/?t={title}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"Error": "Could not fetch info"}

if __name__ == "__main__":
    user_matrix = build_user_item_matrix(load_data(JSON_FILE))
    
    target_user = "Michał B."
    recommendations, anti_recommendations = recommend_movies(user_matrix, target_user)
    
    print(f"\n ---- Top 5 rekomendacji dla {target_user} ----")
    for title in recommendations:
        info = fetch_movie_info(title, OMDB_API_KEY)
        print(f"- {title} ({info.get('Year', '-')}), Gatunek: {info.get('Genre', '-')}, IMDB: {info.get('imdbRating', '-')}")
    
    print(f"\n ---- Top 5 anty-rekomendacji dla {target_user} ----")
    for title in anti_recommendations:
        info = fetch_movie_info(title, OMDB_API_KEY)
        print(f"- {title} ({info.get('Year', '-')}), Gatunek: {info.get('Genre', '-')}, IMDB: {info.get('imdbRating', '-')})")
