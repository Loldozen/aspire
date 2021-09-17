import os
from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    CustomUserSignupSerializer,
    CustomUserLoginSerializer
)


from .authentication import ExternalJWTAuthentication, UserAPIAuthentication
from jwt import decode as jwt_decode
from .models import CustomUser, BlackListedTokens
from lordoftherings.models import Favorite, Character, Quote


class SignupAPIView(APIView):
    """Signup new user"""

    serializer_class = CustomUserSignupSerializer

    #authentication_classes = (ExternalJWTAuthentication,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        if not user:
            return Response(
                {'status': False, 'message': 'User already exists'},
                status=status.HTTP_200_OK,
            )

        user_id = user.id

        return Response(
            {
                'status': True,
                'message': 'User created successfully.',
                'data': {'user_id': user_id},
            },
            status=status.HTTP_201_CREATED,
        )


class LoginAPIView(APIView):
    """Login user"""

    serializer_class = CustomUserLoginSerializer

    #authentication_classes = (ExternalJWTAuthentication,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()
        
        if not user:
            return Response(
                {'status': False, 'message': 'Invalid user account'},
                status=status.HTTP_200_OK,
            )
        
        if user['user'].check_password(user['password']):
            token = user['user'].generate_jwt_token()
            return Response(
                {
                    'status': True,
                    'message': 'User logged in successfully.',
                    'data': {'auth-token': token},
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {
                    'status': False,
                    'message': 'Unable to log in, Invalid User.',
                },
                status=status.HTTP_200_OK,
            )


class LogoutAPIView(APIView):
    """Logout end user"""

    #authentication_classes = (UserAPIAuthentication,)

    def get(self, request):

        auth = request.headers['X-FORWARDED-USER'].split()
        token = auth[1]

        try:
            payload = jwt_decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGO])
            user = CustomUser.objects.get(id=payload.get('id'))
            
        except CustomUser.DoesNotExist:
            return Response(
                {
                    'status': False,
                    'message': 'Unable to logout: Invalid User session.',
                },
                status=status.HTTP_200_OK,
            )

        try:
            BlackListedTokens.objects.get(token=token)
            return Response(
                {
                    'status': False,
                    'message': 'User already logged out.',
                },
                status=status.HTTP_200_OK,
            )
        except BlackListedTokens.DoesNotExist:
            log_out = BlackListedTokens(token=token)
            log_out.save()
            return Response(
                {
                    'status': True,
                    'message': 'User logged out successfully.',
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    'status': False,
                    'message': 'Trouble logging out user, try again later. {}'.format(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

class UserFavoritesAPIView(APIView):
    
    #authentication_classes = (ExternalJWTAuthentication,)

    def get(self, request, user_id):

        try:
            fav = Favorite.objects.get(user=user_id)
        except Favorite.DoesNotExist:
            return Response({'empty_results_errors': ['Favorites Not Found']}, status=status.HTTP_404_NOT_FOUND)
        characters = []
        quotes = []

        for char in fav.character.all():
            characters.append(Character.objects.get(id=char.id))
        for quo in fav.quote.all():
            quotes.append(Quote.objects.get(id=quo.id))

        data = []
        data.append({
            'id':fav.id,
            'user':fav.user.id,
            'characters':characters,
            'quotes':quotes
        })
        return Response(
                {
                    'status': False,
                    'data': data,
                },
                status=status.HTTP_200_OK,
            )