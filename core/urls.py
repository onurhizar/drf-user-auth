from unicodedata import name
from django.urls import path
from .views import TestView, UsersView

urlpatterns = [
    path('test/', TestView.as_view(), name="test view"),
    path('users/', UsersView.as_view(), name="users view"),
]