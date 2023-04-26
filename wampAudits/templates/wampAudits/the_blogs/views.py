from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required

from .forms import Topicform, Articleform
from .models import Topic, Article

def article_protect(Article, request):
    article = Article
    if article.author != request.user:
        raise Http404

def index(request):
    """The home page for the_blogs."""
    return render(request, 'the_blogs/index.html')

def topics(request):
    """show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'the_blogs/topics.html',context)

def topic(request, topic_id):
    """show articles written on a topic."""    
    topic = Topic.objects.get(id=topic_id)
    articles = topic.article_set.order_by('-date_added')
    context = {'topic':topic, 'articles':articles}
    return render(request, 'the_blogs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        #no data submitted, return a blank form
        form = Topicform()
    else:
        #POST data submitted; process data 
        form = Topicform(request.POST)    
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('the_blogs:topics'))

    context = {'form' : form}
    return render(request, 'the_blogs/new_topic.html', context)

@login_required
def new_article(request, topic_id):
    """Add new article for a particular topic"""    
    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        #no data submitted
        form = Articleform()
    else :
        #data submitted, process data
        form = Articleform(request.POST)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.author = request.user
            new_article.topic = topic
            new_article.save()
            return HttpResponseRedirect(reverse("the_blogs:topic", args=[topic_id]))
    context = {'topic': topic, 'form':form}
    return render(request, 'the_blogs/new_article.html', context)

@login_required
def edit_article(request, article_id):
    """Edit an existing article."""
    article = Article.objects.get(id=article_id)
    topic = article.topic
    article_protect(article,request)
    if request.method != 'POST':
        # Initial request; pre-fill form with the current article.
        form = Articleform(instance=article)
    else:
        # POST data submitted; process data.
        form = Articleform(instance=article, data=request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('the_blogs:topic',args=[topic.id]))
    
    context = {'article': article, 'topic': topic, 'form': form}
    return render(request, 'the_blogs/edit_article.html', context)    

def read_article(request, article_id):
    article = Article.objects.get(id=article_id)
    topic = article.topic
    context = {'article':article, 'topic':topic}
    return render(request,'the_blogs/read_article.html',context)
