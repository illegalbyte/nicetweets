from django import forms

class TweetSearchField(forms.Form):
    search_topic = forms.CharField(label='Search Topic', max_length=100)
