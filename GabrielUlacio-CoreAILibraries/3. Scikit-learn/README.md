
# Spotify ML Recommender

Content-based music recommendation system using Scikit-learn. Recommends similar tracks based on audio features using a K-Nearest Neighbors (KNN) model.

## Features
- Content-based recommendations using danceability, energy, valence, tempo, acousticness, and more
- KNN model with cosine similarity
- Genre filtering for more relevant recommendations

## Dataset
The dataset is stored in `data/dataset.csv` and should contain columns such as:
`track_name`, `artists`, `album_name`, `track_genre`, `danceability`, `energy`, `valence`, `tempo`, `acousticness`, etc.
You can use the provided dataset or download a new one from Kaggle (Spotify Tracks Dataset).

## Installation
```bash
git clone https://github.com/your-username/spotify-ml-recommender.git
cd spotify-ml-recommender
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
1. Place your dataset in `data/dataset.csv` (or use the provided one).
2. Run the recommender script:
```bash
python spotify_recommender.py
```
3. The script will print recommendations for the test song defined in the code. You can change the test song and artist in `spotify_recommender.py`.

## Customization
- To get recommendations for a different song, edit the `TEST_SONG` and `TEST_ARTIST` variables in `spotify_recommender.py`.
- Make sure the song exists in your dataset.

## License
MIT
