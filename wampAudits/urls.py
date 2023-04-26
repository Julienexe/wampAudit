"""Defines URL patterns for wampAudits."""
#from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'wampAudits'
urlpatterns = [
    #Home Page
    path('',views.index, name = 'index'),
    #about page
    path('about/', views.about, name='about'),
    #about page
    path('contacts/', views.contacts, name='contacts'),
    # single-post page
    path('single-post/<article_id>',views.single_post, name = 'single-post'),
    # view path for an individual page
    path('topic/<topic_id>', views.topic, name= 'topic'),
]