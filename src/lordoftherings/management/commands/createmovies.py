from django.core.management.base import BaseCommand
from lordoftherings.models import Movie, Character, Quote
import json
import requests
from django.utils.text import slugify
from itertools import zip_longest


class Command(BaseCommand):
    help = 'Create movies'

    def handle(self, *args, **kwargs):

        response = requests.get('https://the-one-api.dev/v2/movie', headers={'Authorization': 'Bearer Pnxcg_AGI-lw_nvVF0dt'})
        data = response.json()

        for mov in data['docs']:
            try :
                movie = Movie.objects.get(_id=mov['_id'])
                print("Movie with name {} already exists".format(movie.name))
            except Movie.DoesNotExist:
                print("Creating movie {}".format(mov['name']))
                movie = Movie.objects.create(
                    _id=mov['_id'],
                    name=mov['name'],
                    runtimeInMinutes=mov['runtimeInMinutes'],
                    budgetInMillions=mov['budgetInMillions'],
                    boxOfficeRevenueInMillions=mov['boxOfficeRevenueInMillions'],
                    academyAwardNominations=mov['academyAwardNominations'],
                    academyAwardWins=mov['academyAwardWins'],
                    rottenTomatoesScore=mov['rottenTomatoesScore']
                )
        