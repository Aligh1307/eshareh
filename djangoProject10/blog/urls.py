from django.urls import path
from .views import word, home, search, add_to_favorites, remove_favorites, my_favorites, autocomplete

urlpatterns = [
    path('autocomplete/', autocomplete, name='autocomplete'),
    path('word/<slug:slug>/', word, name='word'),
    path('search/', search, name='search'),
    path('home/', home, name='home'),
    path('home/<slug:slug>/', home, name='home'),
    path('add_to_favorites/<int:word_id>/', add_to_favorites, name='add_to_favorites'),
    path('remove_favorites/<int:word_id>/', remove_favorites, name='remove_favorites'),
    path('my_favorites/', my_favorites, name='my_favorites')
]
