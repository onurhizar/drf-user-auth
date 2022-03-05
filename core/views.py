from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from .serializers import UserListSerializer, UserRegisterSerializer

# for custom auth token obtainer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .customAuth import authTokenName

# for protected routes
from rest_framework.permissions import IsAuthenticated


class TestView(APIView):
    def get(self, request):
        content = {"msg":"hello"}
        return Response(content)


# get and post for listing or creating users
class UsersView(APIView):
    def get(self, request):
        userList = User.objects.all() # returns a querySet
        serializer = UserListSerializer(userList, many=True) # so we need say many=True
        return Response(serializer.data)

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # if credentials are valid, save to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomAuthTokenObtainView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        content = {
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        }

        cookieSeconds = 60
        header = {'Set-Cookie': f'{authTokenName}={token.key}; Max-Age={cookieSeconds}; HttpOnly'}
        return Response(content, headers=header)


class ProtectedRouteTestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        theUser = request.user # authenticated user as a User model
        content = {"msg": f"welcome {theUser.username} to the protected area"}
        return Response(content)