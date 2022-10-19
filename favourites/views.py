from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from ShopApp.models import Product
from ShopApp.utils import menu
from cart.forms import CartAddProductForm
from .favourites import Favourites

"""
add_to_favourites - Добавление товара в список избранного.
favourites_list - Отображения списка избранного, empty - нужен для проверки на то, пустой список или нет,
так же добавляем CartAddProductForm для перенаправления на покупку товара.
remove_from_favourites - Удаление товара из списка избранного.
"""


@require_POST
def add_to_favourites(request, product_id):
    favourites = Favourites(request)
    product = get_object_or_404(Product, id=product_id)
    favourites.add(product=product)
    return redirect('favourites:favourites_list')


def favourites_list(request):
    favourites = Favourites(request)
    empty = True

    for item in favourites:
        if (item['price'] == 0) and (item['name'] == 0):
            empty = True
        else:
            empty = False

    context = {
        'favourites': favourites,
        'menu': menu,
        'empty': empty,
        'title': 'Избранное',
        'cart_product_form': CartAddProductForm,
    }
    return render(request, 'favourites/list.html', context=context)


def remove_from_favourites(request, product_id):
    cart = Favourites(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('favourites:favourites_list')
