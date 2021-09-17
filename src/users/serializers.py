from rest_framework import serializers
from django.core.serializers.json import DjangoJSONEncoder

from rest_framework.response import Response
from rest_framework import status

from .models import CustomUser

from django.contrib.auth.hashers import make_password

class CustomUserSignupSerializer(serializers.Serializer):
    """Sign up user"""

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def create(self, validated_data):

        try:
            CustomUser.objects.get(email=validated_data['email'])
            return False
        except CustomUser.DoesNotExist:
            hashed_password = make_password(validated_data['password'])
            user = CustomUser(
                email=validated_data['email'],
                username=validated_data['username'],
                password=hashed_password,
                )
            user.save()
            return user


class CustomUserLoginSerializer(serializers.Serializer):
    """Sign in user"""

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def create(self, validated_data):
        """Overridden."""
        try:
            user = CustomUser.objects.get(email=validated_data['email'])
            return {'user':user, 'password': validated_data['password']}
        except CustomUser.DoesNotExist:
            return False
