import json
import time
from threading import Thread

# pandas managing dataframes
import pandas as pd

# django core
from django.shortcuts import get_object_or_404, redirect, render

# API endpoint for sentiment analysis:
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TweetSerializer


from nicetweetsapp.forms import TweetSearchField
from . import filteredstream_API
from .models import Tweet

# Create your views here.

def index(request):
    # if this is a post request, process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TweetSearchField(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            redirect('nicetweetsapp/topicsentiment')
    else:
        # if a GET (or any other method) we'll create a blank form
        form = TweetSearchField()

    return render(request, 'nicetweetsapp/index.html', {'form': form})


def topicsentiment(request):
    # display the topic at the top of the page
    topic = request.POST.get('search_topic')

    # begin stream of tweets in a thread and save to database
    def start_saving_tweets():
        filteredstream_API.main(topic)
    
    # start the twitter request in a separate thread
    Thread(target=start_saving_tweets).start()

    time.sleep(10)
    # get the tweets from the database
    item = Tweet.objects.filter(topic=topic).values()
    df = pd.DataFrame(item)
    df1 = df['created_at']
    pd.to_datetime('1970-01-01').value
    df1 = df['created_at'].apply(lambda x: pd.to_datetime(x).value)
    df1 = df1.tolist()
    df = df['sentiment'].tolist()

    return render(request, 'nicetweetsapp/topicsentiment.html', {'topic': topic, 'sentiment': df, 'timecreated': df1})
    return render(request, 'nicetweetsapp/topicsentiment.html', {'topic': topic, 'df_sentiment': df_sentiment, 'df_time': df_time})

'''
def topicsentiment_api(request):
    def get_tweet_topic_sentiment(topic):

    
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            sentimentjson = json.dumps(T)

'''


class TweetAPIViews(APIView):
    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status': 'ok', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({status: 'error', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, topic=None):
        if topic is None:
            tweets = Tweet.objects.all()
            serializer = TweetSerializer(tweets, many=True)
            return Response({'status': 'ok', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            tweets = Tweet.objects.filter(topic=topic)
            serializer = TweetSerializer(tweets, many=True)
            return Response({'status': 'ok', 'data': serializer.data}, status=status.HTTP_200_OK)


