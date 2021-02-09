from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
  post_title = models.CharField(max_length=150)
  post_publish_date = models.DateTimeField(default=timezone.now)
  post_content = models.TextField()
  post_author = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.post_title
  
  def get_absolute_url(self):
      return reverse("post-detail", kwargs={"slug": self.post_title})
  