from django.urls import path

from .views import (
    ListCharactersAPIView,
    CharacterQuotesAPIView,
    CreateCharacterFavorite,
    CreateQuoteFavorite,
)

urlpatterns = [
    path('character/', ListCharactersAPIView.as_view(), name='character_list'),
    path('character/<str:character_id>/quote/', CharacterQuotesAPIView.as_view(), name='character_quotes'),
    path('character/favorites/', CreateCharacterFavorite.as_view(), name='like_character'),
    path('character/quotes/favorites/', CreateQuoteFavorite.as_view(), name='like_quote'),
]