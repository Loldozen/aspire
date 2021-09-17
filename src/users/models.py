from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from datetime import datetime, timedelta
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import uuid
import jwt

from .managers import CustomUserManager
# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=False)
    created_datetime = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_datetime = models.DateTimeField(_('Last update at'), auto_now=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        """Respresentation of CustomUser."""

        return 'User| {} - {}'.format(self.username, self.email)

    def generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 30 days into the future.
        """
        dt = datetime.now() + timedelta(days=30)

        token = jwt.encode({
            'id': str(self.id),
            'exp': int(dt.strftime('%s'))
        }, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGO)

        return token.decode('utf-8')

class BlackListedTokens(models.Model):
    """Model that represent black listed user access tokens."""

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    token = models.CharField(max_length=500)
    created_datetime = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_datetime = models.DateTimeField(_('Last update at'), auto_now=True)
    objects = models.Manager()

    def __str__(self):
        """Representation for black listed token."""
        return 'Token {}'.format(self.token)
