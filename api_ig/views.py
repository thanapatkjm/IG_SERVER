from django.shortcuts import render
from django.utils import timezone
from rest_framework.viewsets import ModelViewSet
from django.http import Http404

from .models import UserImage, Comment
from .serializers import Get_userimage ,Get_comment
from django.http import JsonResponse


class Comment_viewSet(ModelViewSet):
    # queryset = Comment.objects.all()
    serializer_class = Get_comment   
    def get_queryset(self):
        req = self.request
        post_id = req.query_params.get('id')
        if post_id:
            self.queryset = Comment.objects.filter(id=post_id)
            return self.queryset
        else:
            raise Http404("There is something wrong about this content!")
    

class Userimage_viewSet(ModelViewSet):
    serializer_class = Get_userimage
    def get_queryset(self):
        req = self.request  
        user_id = req.query_params.get('user')
        if user_id:
            self.queryset =  UserImage.objects.filter(user=user_id)
            return self.queryset
        else:
            self.queryset = UserImage.objects.all()
            return self.queryset



