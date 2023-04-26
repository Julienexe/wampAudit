from django.forms import ModelForm
from django import forms
from .models import Comment, Reply, Message

class Commentform(ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','text']

class Messageform(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'