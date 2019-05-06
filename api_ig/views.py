from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import status


from .models import UserImage, Comment
from .serializers import Get_userimage ,Get_comment,Create_User
from django.http import JsonResponse
import json
from django.contrib.auth.models import User as UserAuth

class Register(APIView):
    def post(self, request, *args, **kwargs):
        print("7777777777777777777777777777")
        print(request.body)
        json_data = json.loads(request.body)
        print(json_data['password'])
        create_user = Create_User(data=json_data)
        if create_user.is_valid():
            print("111111111111111111111111111")
            create_user.save()
            return Response(create_user.data, status=status.HTTP_201_CREATED)
        else:
            print("000000000000000000000000000")
            return Response(create_user.errors, status=status.HTTP_400_BAD_REQUEST)

class Get_Auth(APIView):
    def get(self,request):
        username = self.request.query_params.get('username')
        password = self.request.query_params.get('password')
        print(username+"   "+password)

class Userimage_viewSet(APIView):
    def get(self,request):
        user_id = self.request.query_params.get('user')
        if user_id:
            data_send =  UserImage.objects.filter(user=user_id)
            serializer = Get_userimage(data_send, many=True)
            return Response(serializer.data)
        else:
            data_send =  UserImage.objects.order_by('-time_post')
            serializer = Get_userimage(data_send, many=True)
            return Response(serializer.data)

    def post(self,request):
        userimage = Get_userimage(data=request.data)
        if userimage.is_valid():
            userimage.save()
            return Response(userimage.data, status=status.HTTP_201_CREATED)

        else:
            return Response(userimage.errors, status=status.HTTP_400_BAD_REQUEST)



class Comment_viewSet(APIView): 
    def get(self,request):
        post_id = self.request.query_params.get('post_id')
        if post_id:
            data_send =  Comment.objects.filter(post_id=post_id)
            serializer = Get_comment(data_send, many=True)
            return Response(serializer.data)
        else:
            data_send =  Comment.objects.all()
            serializer = Get_comment(data_send, many=True)
            return Response(serializer.data)

    def post(self,request):
        username = self.request.user.get_username()
        if username:
            Comment.objects.create()
            print("user = :"+username)
            serializer.save(user=username)



# class Comment_viewSet(ModelViewSet):
#     # queryset = Comment.objects.all()
#     serializer_class = Get_comment   
#     def perform_create(self, serializer):
#         username = self.request.user.get_username()
#         if username:
#             print("user = : "+username)
#             serializer.save(user=username)
#         else:
#             print("11111111111111111")

#     def get_queryset(self):
#         req = self.request
#         post_id = req.query_params.get('post_id')
#         if post_id:
#             self.queryset = Comment.objects.filter(post_id=post_id)
#             return self.queryset
#         else:
#             raise Http404("There is something wrong about this content!")

# class Userimage_viewSet(ModelViewSet):
#     serializer_class = Get_userimage
#     def get_queryset(self):
#         req = self.request  
#         user_id = req.query_params.get('user')
#         if user_id:
#             self.queryset =  UserImage.objects.filter(user=user_id)
#             return self.queryset
#         else:
#             self.queryset = UserImage.objects.all()
#             return self.queryset
