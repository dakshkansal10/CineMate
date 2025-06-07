# Movie Recommender System Using Machine Learning

## Overview
This project is a content-based movie recommendation system built using Python and Streamlit. The system suggests movies similar to a user-selected movie by analyzing plot descriptions and using machine learning techniques like cosine similarity.

## Features
- **Movie Recommendations**: Recommends top 5 movies similar to the selected movie.
- **Poster Fetching**: Fetches posters of recommended movies using the TMDB API (currently commented out).
- **Streamlit Interface**: Interactive web interface for user-friendly movie selection and recommendations.

## Files and Directory Structure
- **artifacts/**
  - `movie_list_1.pkl`: Pickle file containing the list of movies with their IDs and titles.
  - `similarity.pkl`: Pickle file with precomputed similarity scores between movies.
- **src/**
  - `app.py`: Main application code for running the Streamlit app.
  - `movie-recommender.ipynb`: Jupyter notebook with code to build the recommendation model using techniques like PorterStemmer, CountVectorizer, and cosine similarity.
  - `setup.py`: Setup file to install the package.
  - `README.md`: Project documentation file.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/dakshkansal10/CineMate.git
   ```
2. Navigate to the project directory:
   ```bash
   cd movie-recommender-system
   ```
   
## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run src/app.py
   ```
2. In the app:
   - Select a movie from the dropdown menu.
   - Click **Show Recommendation** to see the top 5 recommended movies.


## Dependencies
- **Python**: Ensure you have Python 3.10 or above.
- **Streamlit**: For creating the interactive web app.
- **Requests**: To fetch movie posters from the TMDB API.
- **Pickle**: To load pre-saved movie data and similarity matrix.

## Model Details
- **Recommendation Technique**: Content-based filtering using CountVectorizer and cosine similarity.
- **Data Preprocessing**: Used PorterStemmer for stemming and vectorized plot descriptions.
- **Similarity Calculation**: Cosine similarity on movie descriptions for recommendation.
