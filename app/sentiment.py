from textblob import TextBlob

def analyze_sentiment(text: str):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # Convert -1 to 1 scale → 0 to 100 trust
    score = (polarity + 1) * 50
    return round(score, 2)