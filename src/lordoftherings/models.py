from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
import uuid
# Create your models here.


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    _id = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    runtimeInMinutes = models.CharField(max_length=100, null=True)
    boxOfficeRevenueInMillions = models.CharField(max_length=100, null=True)
    budgetInMillions = models.CharField(max_length=100, null=True)
    academyAwardNominations = models.CharField(max_length=100, null=True)
    academyAwardWins = models.CharField(max_length=10, null=True)
    rottenTomatoesScore = models.CharField(max_length=100, null=True)
    objects = models.Manager()

    def __str__(self):
        """Respresentation of each book."""

        return 'Movie - {}'.format(self.name)

class Character(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    _id = models.CharField(max_length=255, null=True)
    height = models.CharField(max_length=100, null=True)
    race = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=255, null=True)
    birth = models.CharField(max_length=255, null=True)
    spouse = models.CharField(max_length=255, null=True)
    death = models.CharField(max_length=255, null=True)
    realm = models.CharField(max_length=255, null=True)
    hair = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    wikiUrl = models.CharField(max_length=255, null=True)
    objects = models.Manager()

    def __str__(self):
        """Respresentation of each character."""

        return '{} - {}'.format(self.name, self.race)

class Quote(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    _id = models.CharField(max_length=255, null=True)
    dialog = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        """Respresentation of each quotes by a character."""

        return "By {} in {}".format(self.character.name, self.movie.name)

class Favorite(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    #character = ArrayField(models.CharField(max_length=100), default=list)
    #quote = ArrayField(models.CharField(max_length=100), default=list)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=True)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE)
    slug = models.CharField(max_length=255, null=True)
    objects = models.Manager()

    def __str__(self):
        """Respresentation of the favorites of each user."""

        return 'Favorites of - {}'.format(self.user.username)