from django.core.management.base import BaseCommand
from lordoftherings.models import Character
import json
import requests
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Create characters'

    def handle(self, *args, **kwargs):

        response = requests.get('https://the-one-api.dev/v2/character', headers={'Authorization': 'Bearer Pnxcg_AGI-lw_nvVF0dt'})
        data = response.json()

        for char in data['docs']:
            try :
                character = Character.objects.get(_id=char['_id'])
                print('Character with name {} already exists'.format(character.name))
            except Character.DoesNotExist:
                if 'wikiUrl' and 'gender' not in char.keys():
                    """because of inconsistent data from the api"""
                    continue 
                print("creating character {}".format(char['name']))
                character = Character.objects.create(
                    _id=char['_id'],
                    name=char['name'],
                    height=char['height'],
                    race=char['race'],
                    gender=char['gender'],
                    birth=char['birth'],
                    spouse=char['spouse'],
                    death=char['death'],
                    realm=char['realm'],
                    hair=char['hair'],
                    wikiUrl=char['wikiUrl'],
                )