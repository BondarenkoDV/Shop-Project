from django.urls import path
from .views import CreateCheckoutSessionView

app_name = 'payments'

urlpatterns = [
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
]
