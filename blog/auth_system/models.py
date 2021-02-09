from django.db import models
from django.contrib.auth.models import User
from PIL import Image
class profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  img = models.ImageField(upload_to="profile's_pics",default="profile's_pics/default.jpg")
  score = models.IntegerField(default=0)
  def __str__(self):
      return f"{self.user.username}'s profile"
  def save(self, *args, **kwargs):
    super(profile, self).save(*args, **kwargs)
    
    aimg = Image.open(self.img.path)
    
    if aimg.width > 250 or aimg.height > 250:
      aimg.thumbnail((250,250))
      aimg.save(self.img.path)
