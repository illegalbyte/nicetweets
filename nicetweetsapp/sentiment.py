import textblob
from nltk.sentiment import SentimentIntensityAnalyzer

def get_sentiment(text):
    sentiment = textblob.TextBlob(text).sentiment.polarity
    return sentiment

def nltk_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)['compound']
    return sentiment