from django.urls import path, include
from . import views

urlpatterns = [
    path('api/get_userdata/',views.Userimage_viewSet.as_view()),
    path('api/get_comment/',views.Comment_viewSet.as_view()),
    path('api/regis/',views.Register.as_view()),
    path('api/get_auth/',views.Get_Auth.as_view()),
]
