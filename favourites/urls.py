from .views import *
from django.urls import path

app_name = 'favourites'

urlpatterns = [
        path('', favourites_list, name='favourites_list'),
        path('add/<int:product_id>/', add_to_favourites, name='add_to_favourites'),
        path('remove/<int:product_id>/', remove_from_favourites, name='remove_from_favourites'),
]
