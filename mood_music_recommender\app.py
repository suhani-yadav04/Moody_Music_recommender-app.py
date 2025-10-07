@ -0,0 +1,24 @@
import streamlit as st
from mood_model import detect_mood
from recommender import recommend_songs

st.set_page_config(page_title="Mood-Based Music Recommender 🎶", layout="centered")

st.title("🎧 Mood-Based Music Recommender")
st.write("Type how you feel, and I'll suggest songs for your vibe.")

user_input = st.text_area("How are you feeling today?")

if st.button("Recommend Songs"):
    if user_input.strip() == "":
        st.warning("Please type something!")
    else:
        mood = detect_mood(user_input)
        st.subheader(f"Detected Mood: **{mood.capitalize()}**")
        recommendations = recommend_songs(mood)

        for song in recommendations:
            if isinstance(song, dict):
                st.markdown(f"🎵 **{song['title']}** by *{song['artist']}* → [Listen here]({song['link']})")
            else:
                st.warning(song)
