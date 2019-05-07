from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/get_userdata/',views.Userimage_viewSet.as_view()),
    path('api/get_comment/',views.Comment_viewSet.as_view()),
    path('api/regis/',views.Register.as_view()),
    path('api/get_auth/',views.Get_Auth.as_view()),
    path('api/get_all_user/',views.Get_all_user.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
