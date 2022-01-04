from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topicsentiment', views.topicsentiment, name='topicsentiment'),
    path('api/topicsentiment', views.topicsentiment_api, name='topicsentiment_api'),
]
