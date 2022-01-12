from django.test import TestCase
from django.utils import timezone
from .models import Tweet
from . import filteredstream_API

# Create your tests here.

class SavingTweetsTests(TestCase):

    def test_saving_tweet_to_database(self):
        '''
        Test saving tweets to the sqlite database
        '''
        tweet = Tweet(text='Hello world', sentiment=0.0, created_at=timezone.now())
        tweet.save()

        saved_tweet = Tweet.objects.get(text='Hello world')
        self.assertEqual(saved_tweet.text, 'Hello world')
        self.assertEqual(saved_tweet.sentiment, 0.0)

    def test_saving_tweet_to_database_with_sentiment(self):
        '''
        Test saving tweets to the sqlite database with sentiment
        '''
        tweet = Tweet(text='Hello world', sentiment=0.0, created_at=timezone.now())
        tweet.save()

        saved_tweet = Tweet.objects.get(text='Hello world')
        self.assertEqual(saved_tweet.text, 'Hello world')
        self.assertEqual(saved_tweet.sentiment, 0.0)

    def test_saving_tweet_to_database_with_sentiment_and_time(self):
        '''
        Test saving tweets to the sqlite database with sentiment and time
        '''
        tweet = Tweet(text='Hello world', sentiment=0.0, created_at=timezone.now())
        tweet.save()

        saved_tweet = Tweet.objects.get(text='Hello world')
        self.assertEqual(saved_tweet.text, 'Hello world')
        self.assertEqual(saved_tweet.sentiment, 0.0)

''' THESE TESTS WON'T WORK BECAUSE OF THE INFINITE LOOP OF THE TWITTER API BEING CALLED
# THEY ALSO CANNOT BE CALLED ON GITHUB ACTIONS DUE TO THE LACK OF AN API KEY
class FilteredStreamTests(TestCase):

    def test_filtered_stream_API(self):

        # Test the filtered stream API

        topic = 'test'
        filteredstream_API.main(topic)
        self.assertEqual(Tweet.objects.filter(topic=topic).count(), 0)

    def test_filtered_stream_API_with_sentiment(self):

        # Test the filtered stream API with sentiment

        topic = 'test'
        filteredstream_API.main(topic)
        self.assertEqual(Tweet.objects.filter(topic=topic).count(), 0)

    def test_filtered_stream_API_with_sentiment_and_time(self):

        # Test the filtered stream API with sentiment and time

        topic = 'test'
        filteredstream_API.main(topic)
        self.assertEqual(Tweet.objects.filter(topic=topic).count(), 0)
'''

