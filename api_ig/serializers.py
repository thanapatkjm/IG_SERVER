from rest_framework import serializers
from .models import UserImage, Comment
from django.contrib.auth.models import User

class Get_userimage(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = ('user', 'descrip', 'time_post','image')

class Get_comment(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'comm', 'time_post','post')