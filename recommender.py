
import pandas as pd
import random

def recommend_songs(mood, data_path="data/songs.csv"):
    df = pd.read_csv("songs.py")
    mood_songs = df[df['mood'] == mood]

    if mood_songs.empty:
        return ["No songs found for this mood. Try again!"]

    return mood_songs.sample(min(3, len(mood_songs))).to_dict(orient="records")
