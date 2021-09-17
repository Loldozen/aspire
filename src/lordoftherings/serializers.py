from rest_framework import serializers
from django.core.serializers.json import DjangoJSONEncoder


from .models import Favorite


class CharacterFavoriteSerializer(serializers.Serializer):
    user = serializers.CharField(required=True)
    character = serializers.CharField(allow_null=True)

    def create(self, validated_data):
    
        try:
            fav = Favorite.objects.get(user=validated_data['user'])
        except Favorite.DoesNotExist:
            fav = Favorite(
                user=validated_data['user'],
                )
            fav.character.add(validated_data['character'])
            fav.save()
            return fav
        else:
            fav.character.add(validated_data['character'])
            fav.save()
            return fav

class QuoteFavoriteSerializer(serializers.Serializer):
    user = serializers.CharField(required=True)
    quote = serializers.CharField(allow_null=True)
    character = serializers.CharField(allow_null=True)

    def create(self, validated_data):
    
        try:
            fav = Favorite.objects.get(user=validated_data['user'])
        except Favorite.DoesNotExist:
            fav = Favorite(
                user=validated_data['user'],
                )
            fav.quote.add(validated_data['quote'])
            fav.character.add(validated_data['character'])
            fav.save()
            return fav
        else:
            fav.quote.add(validated_data['quote'] )
            fav.character.add(validated_data['character'])
            fav.save()
            return fav