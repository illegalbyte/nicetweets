from rest_framework import serializers
from nicetweetsapp.models import Tweet
import pandas as pd
import time

# for converting timestamp to an integer and vice versa
class TimestampField(serializers.Field):
    def to_representation(self, value):
        return int(time.mktime(value.timetuple())*1000)

    def to_internal_value(self, data):
        return pd.to_datetime(data)

# serialiser for the tweet model to be used in the api
# serialiser converts the model into a json object
class TweetSerializer(serializers.ModelSerializer):

    tweet_text = serializers.CharField(source='text')
    tweet_sentiment = serializers.FloatField(source='sentiment')
    tweet_created_at = TimestampField(source='created_at')
    tweet_topic = serializers.CharField(source='topic')


    class Meta:
        model = Tweet
        fields = ('tweet_text', 'tweet_sentiment', 'tweet_created_at', 'tweet_topic')