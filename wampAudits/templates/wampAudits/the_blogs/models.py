from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """a topic a user is writing about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """returns a string representation of the model."""
        return self.text

class Article(models.Model):
    """Something written about a topic"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default='Article')
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
 
    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."
