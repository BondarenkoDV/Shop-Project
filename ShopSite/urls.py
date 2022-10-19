from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from ShopSite import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('cart/', include('cart.urls', namespace='cart')),
                  path('checkout/', include('payments.urls', namespace='payments')),
                  path('', include('ShopApp.urls', namespace='shop')),
                  path('favourites/', include('favourites.urls', namespace='favourites')),
                  path('feedback/', include('feedback.urls', namespace='feedback')),
                  path('account/', include('account.urls', namespace='account'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
