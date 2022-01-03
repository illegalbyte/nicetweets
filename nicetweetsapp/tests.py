from django.test import TestCase
from django.utils import timezone
from .models import Tweet

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