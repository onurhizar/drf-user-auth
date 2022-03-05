from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from .serializers import UserListSerializer, UserRegisterSerializer


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


