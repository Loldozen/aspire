import os
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header

from .models import  BlackListedTokens

from jwt import decode as jwt_decode
from jwt import encode as jwt_encode
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError




class UserAPIAuthentication(BaseAuthentication):
    """Token Authentication for end user interaction."""

    def authenticate(self, request):
        """Authenticate user token."""

        payload = {}
        if os.environ['DJANGO_SETTINGS_MODULE'] != 'aspire.settings.dev':
            try:
                auth = request.headers.get('X-FORWARDED-USER', None).split()
            except Exception as e:
                msg = 'Invalid basic header: (X-FORWARDED-USER) not found'
                raise exceptions.AuthenticationFailed(msg)

            if auth[0].lower() != 'bearer':
                msg = "Invalid basic header: 'bearer' scheme not found"
                raise exceptions.AuthenticationFailed(msg)

            if len(auth) == 1:
                msg = 'Invalid basic header. No credentials provided.'
                raise exceptions.AuthenticationFailed(msg)

            if len(auth) > 2:
                msg = 'Invalid basic header. Credentials string should not contain spaces.'
                raise exceptions.AuthenticationFailed(msg)

            token = auth[1]

            try:
                payload = jwt_decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGO])
            except ExpiredSignatureError:
                msg = 'Expired token.'
                raise exceptions.AuthenticationFailed(msg)
            except InvalidTokenError:
                msg = 'Invalid token.'
                raise exceptions.AuthenticationFailed(msg)

            try:
                BlackListedTokens.objects.get(token=token)
                msg = 'You are logged out. Try logging in!'
                raise exceptions.AuthenticationFailed(msg)
            except BlackListedTokens.DoesNotExist:
                return True, payload


class ExternalJWTAuthentication(BaseAuthentication):
    """Authentication class for jwt validation."""

    def authenticate(self, request):
        """Authenticate jwt token."""

        payload = {}
        if os.environ['DJANGO_SETTINGS_MODULE'] != 'aspire.settings.dev':
            auth = get_authorization_header(request).split()

            if not auth or auth[0].lower() != b'bearer':
                try:
                    auth = request.headers.get('X-Authorization', None).split()
                    if not auth[0].lower() == 'bearer':
                        msg = 'Invalid basic header 1.'
                        raise exceptions.AuthenticationFailed(msg)
                except AttributeError:
                    msg = 'Invalid basic header 2.'
                    raise exceptions.AuthenticationFailed(msg)

            if len(auth) == 1:
                msg = 'Invalid basic header. No credentials provided.'
                raise exceptions.AuthenticationFailed(msg)

            if len(auth) > 2:
                msg = 'Invalid basic header. Credentials string should not contain spaces.'
                raise exceptions.AuthenticationFailed(msg)

            token = auth[1]

            try:
                payload = jwt_decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGO])
            except InvalidTokenError:
                msg = 'Invalid token.'
                raise exceptions.AuthenticationFailed(msg)

            partner = payload.get('partner')
            if not partner or partner not in settings.AUTH_PARTNERS:
                raise exceptions.AuthenticationFailed('Invalid Token')

        return True, payload


def generate_jwt_token(payload):
    """Generate authentication token for external partner."""
    return jwt_encode(payload, settings.JWT_SECRET_KEY, settings.JWT_ALGO).decode('utf-8')
