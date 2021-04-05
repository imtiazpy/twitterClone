from django.urls import path
from .views import (
    home, tweet_detail_view, tweet_list_view,
    tweet_create_view
)

urlpatterns = [
    path('', home, name = 'home'),
    path('create_tweet/', tweet_create_view, name='create'),
    path('tweets/', tweet_list_view, name='list'),
    path('tweet/<int:tweet_id>', tweet_detail_view, name='detail')
]