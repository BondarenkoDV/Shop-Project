from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('', account_detail, name='account_detail'),
]
