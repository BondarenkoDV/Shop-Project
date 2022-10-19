from django.conf import settings
from ShopApp.models import Product
from decimal import Decimal

"""
__init__ - Инициализация списка избранного.
__iter__ - Перебор и получение товаров из бд для списка избранного.
add - Добавление товара в список избранного.
remove - Удаление товара из списка избранного.
save - Сохранение.
clear - Очистка товаров из избранного в сессии.
"""


class Favourites(object):

    def __init__(self, request):

        self.session = request.session
        favourites = self.session.get(settings.FAVOURITE_SESSION_ID)
        if not favourites:
            favourites = self.session[settings.FAVOURITE_SESSION_ID] = {}

        self.favourites = favourites

    def __iter__(self):
        product_ids = self.favourites.keys()
        products = Product.objects.filter(id__in=product_ids)

        favourites = self.favourites.copy()
        for product in products:
            favourites[str(product.id)]['product'] = product

        for item in favourites.values():
            item['price'] = Decimal(item['price'])
            yield item

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.favourites:
            self.favourites[product_id] = {'price': str(product.price)}

        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.favourites:
            del self.favourites[product_id]
            self.save()

    def clear(self):
        del self.session[settings.FAVOURITE_SESSION_ID]
        self.save()
