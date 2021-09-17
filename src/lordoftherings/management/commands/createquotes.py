from django.core.management.base import BaseCommand
from lordoftherings.models import Quote, Movie, Character
import json
import requests


class Command(BaseCommand):
    help = 'Create countries and terminals'

    def handle(self, *args, **kwargs):

        headers = {'Authorization': 'Bearer Pnxcg_AGI-lw_nvVF0dt'}
        response = requests.get('https://the-one-api.dev/v2/quote', headers=headers)
        data = response.json()

        for quo in data['docs']:
            try :
                quote = Quote.objects.get(_id=quo['_id'])
                print('Quote already exists')
            except Quote.DoesNotExist:
                try:
                    movie = Movie.objects.get(_id=quo['movie'])
                except Movie.DoesNotExist:
                    res = requests.get('https://the-one-api.dev/v2/movie/{}'.format(quo['movie']), headers=headers)
                    data = res.json().get('docs')[0]
                    
                    print("creating movie {}".format(data['name']))
                    movie = Movie.objects.create(
                    _id=data['_id'],
                    name=data['name'],
                    runtimeInMinutes=data['runtimeInMinutes'],
                    budgetInMillions=data['budgetInMillions'],
                    boxOfficeRevenueInMillions=data['boxOfficeRevenueInMillions'],
                    academyAwardNominations=data['academyAwardNominations'],
                    academyAwardWins=data['academyAwardWins'],
                    rottenTomatoesScore=data['rottenTomatoesScore']
                )
                try:
                    character = Character.objects.get(_id=quo['character'])
                except Character.DoesNotExist:
                    res = requests.get('https://the-one-api.dev/v2/character/{}'.format(quo['character']), headers=headers)
                    data = res.json().get('docs')[0]
                    print("creating character {}".format(data['name']))

                    character = Character.objects.create(
                        _id=data['_id'],
                        name=data['name'],
                        height=data['height'],
                        race=data['race'],
                        gender=data['gender'],
                        birth=data['birth'],
                        spouse=data['spouse'],
                        death=data['death'],
                        realm=data['realm'],
                        hair=data['hair'],
                        #wikiUrl=data['wikiUrl']
                    )
                print('creating quote')
                quote = Quote.objects.create(
                    _id=quo['_id'],
                    dialog=quo['dialog'],
                    movie=movie,
                    character=character,
                )