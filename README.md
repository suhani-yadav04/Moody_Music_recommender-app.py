# Moody Music Recommender 🎧
Where your emotions meet melodies — a music companion that understands your mood.

It’s a small Streamlit app that takes a mood text input (like “calm”, “sad but hopeful”, “get me pumped”) and returns a ranked list of recommended songs from a small example dataset using TF-IDF + cosine similarity.


---

## 🌤️ Overview

**Mood Music Recommender** is an interactive web app that recommends songs based on your **current mood**.
Whether you’re feeling calm, nostalgic, joyful, or just vibing in between — this app matches your emotions with the perfect playlist.

It uses **natural language similarity** (TF-IDF + cosine similarity) to map mood descriptions to songs and presents you with personalized recommendations, along with album covers and quick links to play them.

Built with **Streamlit** and powered by **Python**, this lightweight app brings a touch of emotion to technology.

---

## ✨ Features

🎵 **Mood-based song suggestions** — just type your mood (“calm but happy”, “rainy night feels”, “workout hype”)
💛 **Beautiful, simple interface** with instant recommendations
📀 **Shows cover art, genre, and mood tags** for each track
🌈 **No API keys required** — all data is local and customizable
⚡ **Fast and fun** — runs smoothly even on small setups

---

## 🧠 How It Works

1. You type how you feel — for example:

   * *“chill and sleepy”*
   * *“heartbroken but hopeful”*
   * *“energetic and ready to go”*

2. The app compares your input with song descriptions in the dataset using **TF-IDF vectorization** and **cosine similarity**.

3. It then recommends songs whose “mood tags” and “vibe” most closely match your text.

---



mlit run app.py
```

The app will automatically open in your browser at
👉 [http://localhost:8501](http://localhost:8501)

---

## 🪄 Example Mood Prompts

Try some of these for fun:

| Mood Prompt                | What You’ll Get                     |
| -------------------------- | ----------------------------------- |
| *“happy sunshine morning”* | Uplifting songs full of warmth      |
| *“study focus chill”*      | Calm lo-fi or ambient instrumentals |
| *“nostalgic rainy night”*  | Soft indie or acoustic tunes        |
| *“gym motivation”*         | Energetic, high-BPM beats           |

---

## 🧩 File Structure

```
mood_music_recommender/
│
├── app.py                  # Streamlit main application
├── songs.csv               # Dataset containing songs and moods
├── requir
```

