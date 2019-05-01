from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('get_all_userdata', views.Userimage_viewSet ,base_name='get_all_userdata')

app_name='ResRev'
urlpatterns = [
    path('api/',include(router.urls)),
]
