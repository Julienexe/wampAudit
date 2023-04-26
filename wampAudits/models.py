from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser
)

class UserManager(BaseUserManager):
    #the user manager handles the data stored in the user attributes for each user instance and holds methods for creating new users and superusers
    def create_user(self, name:str, last_name:str , email:str, password:str = None, is_staff=False, is_superuser=False) -> "User":
        """function checks for the required user fields, sets user attributes to their allocated values and creates a normal user"""
        if not email:
            raise ValueError("User must have an email")
        if not name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        
        user = self.model(email=self.normalize_email(email))
        user.name = name
        #user.region = region
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser

        return user

    def create_superuser(self, name: str, email:str, password:str) -> "User":
        '''contains a function similar to the create_user method but missing the last_name attribute'''
        if not email:
            raise ValueError("User must have an email")
        if not name:
            raise ValueError("User must have a first name")
        
        user = self.model(email=self.normalize_email(email))
        user.name = name
        #user.region = region
        #user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        '''user = self.create_user(
            name=name,
            last_name= last_name,
            email= email,
            password=password,
            is_staff=True,
            is_superuser=True
        )'''
        user.save()


'''class to specify new user fields'''
class User(AbstractUser):
    #this class is blueprint of each user instance including their attributes that will be stored in the site
    name = models.CharField(verbose_name="Name", max_length=255)
    last_name = models.CharField(verbose_name="Last Name" , max_length=255)
    password = models.CharField(max_length= 255)
    '''region = models.CharField(max_length=25)'''


    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    username = None
    objects = UserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


class Topic(models.Model):
    #creating the topic model with two fields
    """a topic a user is writing about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    cover_picture = models.ImageField(null=True,blank=True)
    # articles = topic.article.set_all()

    # def __str__(self):
    #     """returns a string representation of the model."""
    #     return self.text

    def __articles__(self):
            #returns all related articles
            return self.articles 

class Article(models.Model):
    #articles have 5 fields and are updated by the staff and superusers
    """Something written about a topic"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE, related_name="articles")
    title = models.CharField(max_length=50, default='Article')
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=75)
    #author = models.ForeignKey(User,on_delete=models.CASCADE)
    article_picture = models.ImageField(null=True,blank=True)

 
    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."

class Comment(models.Model):
    #comment made on an article by readers
    article = models.ForeignKey(Article,on_delete=models.CASCADE,  related_name="comments")
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)

class Reply(models.Model):
    # reply to comments made by either the author or another user
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE, related_name="replies")
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)

    class Meta:
        verbose_name_plural = 'Replies'

class Message(models.Model):
    #messages sent by end users/ enduser feedback
    name = models.CharField(max_length=150)
    email =  models.EmailField()
    subject = models.CharField(max_length=150)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)