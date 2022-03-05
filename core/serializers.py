from rest_framework import serializers
from django.contrib.auth.models import User

# serializer for listing users
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


# serializer to register a user
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']