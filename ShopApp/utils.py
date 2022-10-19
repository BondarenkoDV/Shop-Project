from django.db.models import Count
from django.conf import settings
from cart.forms import CartAddProductForm
from .models import *
"""
Файл является миксином, для отсутсвия дублирования кода.

Здесь бы передаем menu, которое отображается в верхней части сайта, 
в котором так же заданы url'ы для передачи их в шаблон.

Передается форма CartAddProductForm, так как она часто используется.
Передаются Категории.
"""

menu = [{'title': 'Главная', 'url_name': 'shop:home'},
        {'title': "Избранное", 'url_name': 'favourites:favourites_list'},
        {'title': "Обратная связь", 'url_name': 'feedback:contact_form'},
        ]


class Mixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        category = Category.objects.annotate(Count('products'))
        context['menu'] = menu
        context['cart_product_form'] = CartAddProductForm
        context['cats'] = category
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
