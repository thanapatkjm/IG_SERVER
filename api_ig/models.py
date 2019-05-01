from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime    


class UserImage(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    descrip = models.TextField()
    image = models.ImageField(upload_to='images')
    time_post = models.DateTimeField(default=datetime.now)

class Comment(models.Model):
    post = models.ForeignKey(UserImage,on_delete=models.CASCADE)
    user = models.TextField()
    time_post = models.DateTimeField(default=datetime.now)
    comm = models.TextField()
