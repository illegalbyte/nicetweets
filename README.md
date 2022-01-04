# nicetweets 🐥

![Test Workflow](https://github.com/illegalbyte/nicetweets/actions/workflows/django.yml/badge.svg)

A twitter client built with Django which filters tweets using sentiment analysis and only shows positive tweets about a given topic.

## Install dependencies with `pip`

    pip install -r requirements.txt

## Twitter API Authentication

At your terminal env the following command to authenticate with Twitter:

    export BEARER_TOKEN='<your_bearer_token>'

## Tweet Sentiment API

Once tweets have been created by searching a topic using the web UI, the sentiment analysis API can be used to get the sentiment of each tweet. The API is available at `/api/<topic>?format=json` and returns a JSON object:

```json
{
    "status":"ok",
    "data":[
        {
            "tweet_text":"Decided to make the 4 siblings in my Halfpelt series, all of them having their problems, and far from a perfect family! This was as close as I could get to their designs!\n\nIn order they are TwigClaw (F) DoveFoot (M) BlossomMask (F) and WillowStream (F) https://t.co/dd3ZGKDEge https://t.co/YxBe3rEUXo",
            "tweet_sentiment":0.55,
            "tweet_created_at":"2022-01-04T05:18:26.235975+11:00",
            "tweet_topic":"cats"
        },
        {
            "tweet_text":"Tongue out Chewsday ðŸ˜›ðŸŒžðŸ’›\n#CatsOfTwitter #cats #AussieCatsOfTwitter https://t.co/1vTlOpJDEI",
            "tweet_sentiment":0.0,
            "tweet_created_at":"2022-01-04T05:18:29.231611+11:00",
            "tweet_topic":"cats"
        },
        {
            "tweet_text":"...and more than that, MAKE THINGS GO RIGHT with your work and your commitment. DO WHAT YOU LOVE to help others. #cats #kittens #SaveThemAll #AdoptCat #AdoptAShelterCat #AdoptDontShop #AdoptDontBuy #spay #neuter #TNR RT for them EVERY day. You will help them AND yourself! https://t.co/w1TcydxHZs",
            "tweet_sentiment":0.4702380952380952,
            "tweet_created_at":"2022-01-04T05:18:30.101079+11:00",
            "tweet_topic":"cats"
        },
        {
            "tweet_text":"Ronaldo was a amazing player in his prime, but I know cats like Greenwood are pissing themselves watching Ronaldo attempt to dribble and pass",
            "tweet_sentiment":0.6000000000000001,
            "tweet_created_at":"2022-01-04T05:18:30.112483+11:00",
            "tweet_topic":"cats"
        },
        {
            "tweet_text":"All of my cats are having a truly Monday Monday.",
            "tweet_sentiment":0.0,
            "tweet_created_at":"2022-01-04T05:18:33.136829+11:00",
            "tweet_topic":"cats"
        },
        {
            "tweet_text":"I gatti salveranno il cielo stellato dall'attacco della megacostellazione #Starlink https://t.co/BbL5AtbABU",
            "tweet_sentiment":0.0,
            "tweet_created_at":"2022-01-04T05:18:34.149712+11:00",
            "tweet_topic":"cats"
        }
    ]
}
```
<!-- https://www.youtube.com/watch?v=zKij1_sHWAc -->
<!-- https://testdriven.io/blog/django-ajax-xhr/#when-should-you-use-ajax -->
<!-- https://dev.to/nobleobioma/create-a-simple-rest-api-with-django-253p -->
<!-- https://stackabuse.com/creating-a-rest-api-with-django-rest-framework/ -->