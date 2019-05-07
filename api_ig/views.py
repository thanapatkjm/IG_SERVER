from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import authenticate
from .models import UserImage, Comment
from .serializers import Get_userimage ,Get_comment,Create_User
from django.http import JsonResponse
import json
from django.contrib.auth.models import User as UserAuth
from rest_framework.parsers import FileUploadParser


class Get_all_user(APIView):
    def get(self,request):
        all_user = UserAuth.objects.all()
        data_array = []
        for each in all_user:
            data = {"id":each.id,
                    "name":each.username}
            data_array.append(data)
        print(data_array)
        return Response(data_array)

class Register(APIView):
    def post(self, request, *args, **kwargs):
        print(request.body)
        json_data = json.loads(request.body)
        print(json_data['password'])
        create_user = Create_User(data=json_data)
        if create_user.is_valid():
            create_user.save()
            return Response(create_user.data, status=status.HTTP_201_CREATED)
        else:
            return Response(create_user.errors, status=status.HTTP_400_BAD_REQUEST)

class Get_Auth(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        print("000000000000000000000000000")
        auth = authenticate(self.request, username=json.loads(request.body)['username'],
                                     password=json.loads(request.body)['password']),
        print("+++"+json.loads(request.body)['username']+"+++++"+json.loads(request.body)['password'])
        print(auth)
        if auth!=(None,):
            print("111111111111111111111111111")
            use = UserAuth.objects.get(username=json.loads(request.body)['username'])
            user_id = use.id
            return Response({
                'user': json.loads(request.body)['username'],
                'user_id': user_id,
                'token': True
            })
        else:
            print("7777777777777777777777777777")
            return Response({
                'user': json.loads(request.body)['username'],
                'user_id': "",
                'token': False
            })

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
            print("-----------------")
            data = serializer.data
            for eachPic in data:
                user = UserAuth.objects.get(id=eachPic['user'])
                eachPic['username'] = user.username
                print(eachPic)
            return Response(data)

    def post(self,request):
        print(request.data)
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
        
        # user ,comm, post
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
