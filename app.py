import pickle
import streamlit as st
import requests
import os
import numpy as np
import pandas as pd

# Function to fetch poster from TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c1af28ffd4b06a46ca170f88a768abb6&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return None

# Movie recommendation function
def recommend(movie):
    if movie not in movies['title'].values:
        return []

    index = movies[movies['title'] == movie].index[0]

    # Ensure similarity is a NumPy array of floats
    sim_array = np.array(similarity)
    sim_array = sim_array.astype(float)

    distances = list(enumerate(sim_array[index]))
    distances = sorted(distances, reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    for i in distances[1:6]:  # Skip the first (same movie)
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names

# Streamlit UI
st.header('🎬 Movie Recommender System Using Machine Learning')

# Use relative paths (Windows compatible)
movie_list_path = os.path.join('artifacts', 'movie_list_1.pkl')
similarity_path = os.path.join('artifacts', 'similarity.pkl')

# Load data
if os.path.exists(movie_list_path) and os.path.exists(similarity_path):
    movies = pickle.load(open(movie_list_path, 'rb'))
    similarity = pickle.load(open(similarity_path, 'rb'))
else:
    st.error("One or more required files are missing in the 'artifacts/' folder.")
    st.stop()

# Movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "🎥 Type or select a movie from the dropdown",
    movie_list
)

# Show recommendations
if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)

    if recommended_movie_names:
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            col.text(recommended_movie_names[idx])
    else:
        st.warning("No recommendations found for the selected movie.")
