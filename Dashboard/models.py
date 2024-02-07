from django.db import models
import uuid
from Authentication.models import *
from ckeditor.fields import RichTextField 
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from taggit.managers import TaggableManager


class Reviews(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    

class Articles(models.Model):
    name = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to="Article-Thumbnail/")
    writer = models.CharField(max_length=20,null=True,blank=True)
    description = models.TextField()
    content = RichTextField(null=True, blank=True)
    created_at =models.DateField(auto_now_add=True)
    meta_tags = models.TextField()
    meta_description = models.TextField()
    tags = TaggableManager()


class SupportTickets(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField() 
    number = models.CharField(max_length=15)
    comments = models.TextField()
    created=models.DateTimeField(auto_now_add=True)


