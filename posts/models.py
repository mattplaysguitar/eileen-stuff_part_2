from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime
from django.urls import reverse
from django.conf import settings
import uuid

#3rd party
from ckeditor.fields import RichTextField
from .validators import *


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    title = models.CharField(max_length=100,blank=True)
    post_summary = RichTextField(null=True, blank=True,)
    body1 = RichTextField(null=True, blank=True,)
    body2 = RichTextField(null=True, blank=True,)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    video = models.CharField(max_length=50, blank=True)
    cover = models.ImageField(upload_to="images/", null=True, blank=True, height_field=None, width_field=None)
    no_video = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.id})
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=133, blank=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("post-list")
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.id})

    
    
    
    


