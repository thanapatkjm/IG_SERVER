from django.shortcuts import render
from django.utils import timezone
from rest_framework.viewsets import ModelViewSet

from .models import UserImage, Comment
from .serializers import Get_userimage ,Get_comment

class Comment_viewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = Get_comment

class Userimage_viewSet(ModelViewSet):
    queryset = UserImage.objects.all()
    serializer_class = Get_userimage




