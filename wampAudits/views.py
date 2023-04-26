from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required

from .forms import Commentform, Messageform
from .models import Topic, Article

#sfunction based views for different blog pages
def index(request):
    """The home page for wampAudits."""
    #index displays info about all topics and most articles 
    topics = Topic.objects.order_by('date_added')
    articles = Article.objects.order_by('topic')
    context = {'topics':topics, 'articles':articles}
    return render(request, 'wampAudits/index.html', context)

# the home page
def base(request):
    """content loaded for the base file"""  
    topics = Topic.objects.order_by('date_added')
    articles = Article.objects.order_by('topic')
    context = {'topics':topics, 'articles':articles}
    return render(request, 'wampAudits/base.html', context)  
    
# page for individual articles
def single_post(request, article_id):
    """The article page for wampAudits."""
    article = Article.objects.get(id=article_id)
    topics = Topic.objects.all()
    posts = Article.objects.all()
    comment_form = Commentform()

    # here's the logic for posting comments made by users
    if request.method == "POST":
        form =  Commentform(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.article = article
            new_comment.save()
            return HttpResponseRedirect(reverse('wampAudits:single-post', args=[article_id]))
    else:
        comment_form = Commentform()    
    context = {'article':article, 'topics':topics, 'posts':posts, 'form':comment_form}    
    return render(request, 'wampAudits/single-post.html', context)

#individual topic page 
def topic(request,  topic_id):
    # here we pick all articles
    posts = Article.objects.all()
    # here we pick the specific category/topic
    topic = Topic.objects.get(id = topic_id)
    # the query below brings all topics from the database
    topics = Topic.objects.all()
    context  = {'posts':posts, 'topic':topic, 'topics':topics}
    return render(request, 'wampAudits/topic.html', context)

def contacts(request):
    """The contacts page for wampAudits."""
    #the form for sending messages to the team
    # messageform = Messageform()
    if request.method == 'POST':
        form = Messageform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('wampAudits:contacts'))
    else:
        form = Messageform()
    context = {'form':form}

    return render(request, 'wampAudits/contact.html', context)

def about(request):
    """The info page for wampAudits."""
    return render(request, 'wampAudits/about.html')