from django.urls import path
from .views import TestView, UsersView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('test/', TestView.as_view(), name="test view"),
    path('users/', UsersView.as_view(), name="users view"),
    path('gettoken/', obtain_auth_token),
]