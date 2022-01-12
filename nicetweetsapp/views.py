import time
from threading import Thread
from numpy import NaN

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
	# OPTION: Delete all tweets on index page load
	if (False):
		Tweet.objects.all().delete()
		print("-\n-\n-\n ->> Deleting all tweets <<- \n-\n-\n-")

	return render(request, 'nicetweetsapp/index.html', {'form': form})


def topicsentiment(request):
	# display the topic at the top of the page
	topic = request.POST.get('search_topic')

	# begin stream of tweets in a thread and save to database
	def start_saving_tweets():
		filteredstream_API.main(topic)
	
	# start the twitter request in a separate thread
	Thread(target=start_saving_tweets).start()

	# make sure data exists before returning response to prevent key error
	sample_response = Tweet.objects.filter(topic=topic).values()
	while sample_response.count() == 0:
		time.sleep(0.1)
		sample_response = Tweet.objects.filter(topic=topic).values()

	# get the tweets from the database and store them in a dataframe
	item = Tweet.objects.filter(topic=topic).values()
	df = pd.DataFrame(item)
	df1 = df['created_at']
	pd.to_datetime('1970-01-01').value
	df1 = df['created_at'].apply(lambda x: pd.to_datetime(x).value)
	df1 = df1.tolist()
	df = df['sentiment'].tolist()

	return render(request, 'nicetweetsapp/topicsentiment.html', {'topic': topic, 'sentiment': df, 'timecreated': df1})

def nicetimeline(request):
	return render(request, 'nicetweetsapp/nicetimeline.html')


class TweetAPIViews(APIView):

	def get(self, request, topic=None):

		if topic is None:
			# if no topic is specified, return all tweets
			tweets = Tweet.objects.all()
			serializer = TweetSerializer(tweets, many=True)
			return Response({'status': 'ok', 'data': serializer.data}, status=status.HTTP_200_OK)
		if topic is not None:
			# if a topic is specified, return all tweets for that topic
			tweets = Tweet.objects.filter(topic=topic)
			serializer = TweetSerializer(tweets, many=True)
			df = pd.DataFrame(serializer.data)
			df['MA'] = df.get('tweet_sentiment').rolling(window=10).mean().fillna(0)
			rolling_average = df['MA'].tolist()
			# handle ajax request
			is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
			if is_ajax:
				return JsonResponse({'status': 'ok', 'data': serializer.data, 'rolling_average': rolling_average}, status=status.HTTP_200_OK)
			else: # handle regular API request
				return Response({'status': 'ok', 'data': serializer.data, 'rolling_average': rolling_average}, status=status.HTTP_200_OK)


