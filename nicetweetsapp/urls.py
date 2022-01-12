from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topicsentiment', views.topicsentiment, name='topicsentiment'),
    path('api/', views.TweetAPIViews.as_view(), name='api'),
    path('api/<str:topic>', views.TweetAPIViews.as_view(), name='api'),
    path('nicetimeline', views.nicetimeline, name='nicetimeline'),
]
