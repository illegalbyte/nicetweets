import textblob


def get_sentiment(text):
    sentiment = textblob.TextBlob(text).sentiment.polarity
    return sentiment