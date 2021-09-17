from django.shortcuts import render
from .models import Character,  Quote, Favorite
from users.authentication import ExternalJWTAuthentication
import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CharacterFavoriteSerializer, QuoteFavoriteSerializer

# Create your views here.
class ListCharactersAPIView(APIView):
    
    #authentication_classes = (ExternalJWTAuthentication,)

    def get(self, request):
        """Get all characters."""

        #response = requests.get('https://the-one-api.dev/v2/character', headers={'Authorization': 'Bearer Pnxcg_AGI-lw_nvVF0dt'})
        #data = response.json()['docs']

        characters = Character.objects.order_by('-name')

        data = []
        for char in characters:
            data.append({'id': char.id, 
            'name': char.name, 
            'height': char.height, 
            'race':char.race, 
            'gender':char.gender, 
            'birth':char.birth, 
            'spouse':char.spouse, 
            'death':char.death,
            'realm':char.realm,
            'hair':char.hair,
            'wikiUrl':char.wikiUrl
            })

        response_payload = {
            'status': True,
            'data': data,
            'total': characters.count(),
        }
        return Response(response_payload, status=status.HTTP_200_OK)

class CharacterQuotesAPIView(APIView):
    
    #authentication_classes = (ExternalJWTAuthentication,)

    def get(self, request, character_id):
        """Get all quotes from a character"""
        
        try :
            character = Character.objects.get(id=character_id)
        except Character.DoesNotExist:
            return Response({'empty_results_errors': ['Character Not Found']}, status=status.HTTP_404_NOT_FOUND)

        quotes = Quote.objects.filter(character=character_id)

        data = []
        for quo in quotes:
            data.append({
                'id':quo.id,
                'dialog':quo.dialog,
                'movie':quo.movie,
            })

        response_payload = {
            'status': True,
            'character': character.name,
            'quotes': data,
            'total':quotes.count()
        }
        print(response_payload)

        return Response(response_payload, status=status.HTTP_200_OK)


class CreateCharacterFavorite(APIView):
    
    serializer_class = CharacterFavoriteSerializer
    #authentication_classes = (ExternalJWTAuthentication,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
           
        try:
            fav = Favorite.objects.get(user=serializer.validated_data['user'])
        except Favorite.DoesNotExist:
            fav = Favorite(
                user=serializer.validated_data['user'],
                )
            fav.character.add(serializer.validated_data['character'])
            fav.save()
        else:
            fav.character.add(serializer.validated_data['character'])
            fav.save()
            print(fav)

        return Response(
            {
                'status': True,
                'message': 'Character liked successfully',
            },
            status=status.HTTP_201_CREATED,
        )

class CreateQuoteFavorite(APIView):

    serializer_class = QuoteFavoriteSerializer
    #authentication_classes = (ExternalJWTAuthentication,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            fav = Favorite.objects.get(user=serializer.validated_data['user'])
        except Favorite.DoesNotExist:
            fav = Favorite(
                user=serializer.validated_data['user'],
                )
            fav.character.add(serializer.validated_data['character'])
            fav.quote.add(serializer.validated_data['quote'])
            fav.save()
        else:
            fav.character.add(serializer.validated_data['character'])
            fav.quote.add(serializer.validated_data['quote'])
            fav.save()

        return Response(
            {
                'status': True,
                'message': 'Quote liked successfully',
            },
            status=status.HTTP_201_CREATED,
        )