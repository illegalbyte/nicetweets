from rest_framework import serializers
from nicetweetsapp.models import Tweet


# serialiser for the tweet model to be used in the api
# serialiser converts the model into a json object
class TweetSerializer(serializers.ModelSerializer):

    tweet_text = serializers.CharField(source='text')
    tweet_sentiment = serializers.FloatField(source='sentiment')
    tweet_created_at = serializers.DateTimeField(source='created_at')
    tweet_topic = serializers.CharField(source='topic')

    class Meta:
        model = Tweet
        fields = ('tweet_text', 'tweet_sentiment', 'tweet_created_at', 'tweet_topic')