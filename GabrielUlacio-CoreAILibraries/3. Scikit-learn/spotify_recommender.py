"""
Content-Based Music Recommender System using Scikit-learn
--------------------------------------------------------
Dataset: Spotify Tracks Dataset (saved at /data/spotify_tracks.csv)
Features: danceability, energy, valence, tempo, etc.
Model: K-Nearest Neighbors (KNN) with cosine similarity.
"""

"""
Global configuration variables
"""
DATASET_PATH = 'data/dataset.csv'  # Path to the dataset
FEATURES = ['danceability', 'energy', 'valence', 'tempo', 'acousticness']  # Features used for similarity
N_RECOMMENDATIONS = 5  # Number of recommendations to show
N_QUERY_NEIGHBORS = 50  # Number of neighbors to query before filtering

TEST_SONG = "I Ain't Worried"  # Song to test recommendations
TEST_ARTIST = "OneRepublic"  # Artist to test recommendations

import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import ColumnTransformer

def load_data():
    """Load and preprocess the Spotify dataset."""
    try:
        df = pd.read_csv(DATASET_PATH)
        X = df[FEATURES]
        preprocessor = ColumnTransformer([
            ('scaler', MinMaxScaler(), FEATURES)
        ])
        X_processed = preprocessor.fit_transform(X)
        return df, X_processed, preprocessor
    except FileNotFoundError:
        raise FileNotFoundError(f"Dataset not found at '{DATASET_PATH}'.")

def train_model(X):
    """Train KNN model using cosine similarity."""
    model = NearestNeighbors(n_neighbors=N_QUERY_NEIGHBORS, metric='cosine', algorithm='brute')
    model.fit(X)
    return model

def recommend_songs(song_name, df, model, preprocessor):
    """Get top N song recommendations based on audio features, filtered by genre. Optionally filter by artist."""
    def _find_song_index(song_name, artist=None):
        matches = df[df['track_name'].str.lower() == song_name.lower()]
        if artist:
            matches = matches[matches['artists'].str.lower().str.contains(artist.lower())]
        if matches.empty:
            raise IndexError
        return matches.index[0]
    try:
        # Find the song index (by name and optionally artist)
        song_idx = _find_song_index(song_name, artist=None)
        # Get genre of the query song
        query_genre = df.iloc[song_idx]['track_genre']
        # Filter dataframe by genre
        df_genre = df[df['track_genre'] == query_genre].reset_index(drop=True)
        if df_genre.empty:
            raise ValueError(f"No songs of genre '{query_genre}' found in the dataset.")
        # Get features and preprocess
        song_features = df.iloc[song_idx][FEATURES].values.reshape(1, -1)
        song_features_df = pd.DataFrame(song_features, columns=FEATURES)
        # Preprocess only the filtered genre subset
        X_genre = df_genre[FEATURES]
        preprocessor_genre = ColumnTransformer([
            ('scaler', MinMaxScaler(), FEATURES)
        ])
        X_genre_processed = preprocessor_genre.fit_transform(X_genre)
        song_features_processed = preprocessor_genre.transform(song_features_df)
        # Train KNN only on filtered genre
        model_genre = NearestNeighbors(n_neighbors=N_QUERY_NEIGHBORS, metric='cosine', algorithm='brute')
        model_genre.fit(X_genre_processed)
        # Find nearest neighbors (excluding the query song itself)
        distances, indices = model_genre.kneighbors(song_features_processed)
        recommendations = df_genre.iloc[indices[0][1:N_QUERY_NEIGHBORS]]
        # Remove duplicates and exclude the queried song
        recommendations = recommendations.drop_duplicates(subset=['track_name'])
        recommendations = recommendations[recommendations['track_name'].str.lower() != song_name.lower()]
        # Limit to N_RECOMMENDATIONS
        recommendations = recommendations.head(N_RECOMMENDATIONS)
        return recommendations[['track_name', 'artists', 'album_name'] + FEATURES]
    except IndexError:
        raise ValueError(f"Song '{song_name}' not found in the dataset.")

if __name__ == "__main__":
    print("Loading data and training model...")
    df, X, preprocessor = load_data()
    model = train_model(X)

    # Example recommendation
    test_song = TEST_SONG  # Change to any song in the dataset
    test_artist = TEST_ARTIST # Optionally set artist name here
    try:
        print(f"\nFinding recommendations similar to: '{test_song}'")
        recommendations = recommend_songs(test_song, df, model, preprocessor)  # You can pass test_artist as 5th arg
        print(f"\nTop {N_RECOMMENDATIONS} Recommendations:")
        for i, (_, row) in enumerate(recommendations.iterrows(), 1):
            print(f"{i}. {row['track_name']} - {row['artists']}")
    except ValueError as e:
        print(f"Error: {e}")