from textblob import TextBlob

def detect_mood(user_input):
    analysis = TextBlob(user_input)
    polarity = analysis.sentiment.polarity

    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"
