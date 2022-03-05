from django.urls import path
from .views import TestView, UsersView
from .views import CustomAuthTokenObtainView
from .views import ProtectedRouteTestView

urlpatterns = [
    path('test/', TestView.as_view(), name="test view"),
    path('users/', UsersView.as_view(), name="users view"),
    path('gettoken/', CustomAuthTokenObtainView.as_view()),
    path('protected-test/', ProtectedRouteTestView.as_view()),
]