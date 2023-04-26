from django.forms import ModelForm
from django import forms
from .models import Topic, Article

class Topicform(ModelForm):
    class Meta:
        model = Topic
        fields = ['text']

class Articleform(ModelForm):
    class Meta:
        model = Article
        fields = ['title','text']
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

