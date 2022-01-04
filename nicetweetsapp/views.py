from django.shortcuts import render, get_object_or_404, redirect
from nicetweetsapp.forms import TweetSearchField
from .models import Tweet
import pandas as pd
from . import filteredstream_API
from threading import Thread
import json
import time



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

def topicsentiment_api(request):
    return render(request, 'nicetweetsapp/topicsentiment_api.html')