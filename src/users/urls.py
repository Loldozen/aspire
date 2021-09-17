from django.urls import path

from .views import (
    LoginAPIView,
    LogoutAPIView,
    SignupAPIView,
    UserFavoritesAPIView
)

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('favorites/<str:user_id>/', UserFavoritesAPIView.as_view(), name='favorites'),
]