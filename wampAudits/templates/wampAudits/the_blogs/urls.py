"""Defines URL patterns for the_blogs."""
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'the_blogs'
urlpatterns = [
     # Home page
     path('',views.index, name='index'),
     # Topics
     path('topics/', views.topics, name='topics'),
     #detail with articles on each topic
     path('topics/<topic_id>', views.topic, name='topic'),
     #adding a new topic
     path('new_topic/', views.new_topic, name="new_topic"),
     #adding a new article
     path('new_article/<topic_id>', views.new_article, name = "new_article"),
     #eeiting an article
     path('edit_article/<article_id>',views.edit_article,  name="edit_article"),
     #reading an article
     path('read_article/<article_id>', views.read_article, name="read_article"),
]
