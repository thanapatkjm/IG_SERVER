from rest_framework import serializers
from .models import UserImage, Comment
from django.contrib.auth.models import User

class Create_User(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","password","email")

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username']
        ,password=validated_data['password']
        , email=validated_data['email'])
        return user

class Get_userimage(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        # fields = ('user', 'descrip', 'time_post','image')
        fields = "__all__"

class Get_comment(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # fields = ('user', 'comm', 'time_post','post')
        fields = "__all__"
