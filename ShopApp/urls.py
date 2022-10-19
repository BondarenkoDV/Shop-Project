from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<slug:cat_slug>/', Categories.as_view(), name='category'),
    path('products/<slug:product_slug>/', ShowProduct.as_view(), name='product'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('cancel-payment/', CancelView, name=' cancel'),
    path('success-payment/', SuccessView, name='success'),
]
