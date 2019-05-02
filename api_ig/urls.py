from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('get_userdata', views.Userimage_viewSet ,base_name='get_userdata')
router.register('get_comment', views.Comment_viewSet ,base_name='get_comment')


app_name='ResRev'
urlpatterns = [
    path('api/',include(router.urls)),
]
