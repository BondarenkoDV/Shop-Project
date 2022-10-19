from django.shortcuts import render, redirect
from ShopApp.utils import menu


def account_detail(request):
    if request.user.is_authenticated:
        context = {
            'menu': menu,
            'title': 'Личный кабинет',
        }
        return render(request, 'account/account.html', context=context)
    else:
        return redirect('shop:login')
