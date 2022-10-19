from django.urls import path
from .views import *

app_name = 'feedback'

urlpatterns = [
    path('', contact_form, name='contact_form'),
    path('success/', success, name='success'),
]
