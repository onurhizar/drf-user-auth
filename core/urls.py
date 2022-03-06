from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.TestView.as_view(), name="test view"),
    path('users/', views.UsersView.as_view(), name="users view"),
    path('gettoken/', views.CustomAuthTokenObtainView.as_view(), name='token obtainer route'),
    path('protected-test/', views.ProtectedRouteTestView.as_view(), name='protected route test'),
    path('setcookie-test/', views.SetCookieTestView.as_view(), name='set cookie test'),
]