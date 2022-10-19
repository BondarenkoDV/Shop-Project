from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .utils import *


class Home(Mixin, ListView):
    model = Product
    template_name = 'ShopApp/index.html'
    context_object_name = 'unit'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='Магазин'))
        return context

    def get_queryset(self):
        # Оптимизация запросов
        return Product.objects.filter(available=True).select_related('category')


class Categories(Mixin, ListView):
    model = Product
    template_name = 'ShopApp/index.html'
    context_object_name = 'unit'
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['cat_slug'], available=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title=str(c.name), cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


class ShowProduct(Mixin, DetailView):
    model = Product
    template_name = 'ShopApp/show_product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title=context['product']))
        return context


class RegisterUser(Mixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'ShopApp/register.html'
    success_url = reverse_lazy('shop:login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='Регистрация'))
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('shop:home')


class LoginUser(Mixin, LoginView):
    form_class = LoginUserForm
    template_name = 'ShopApp/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title='Авторизация'))
        return context

    def get_success_url(self):
        return reverse_lazy('shop:home')


def logout_user(request):
    logout(request)
    return redirect('shop:home')


def SuccessView(request):
    context = {
        'title': 'Успех',
    }
    return render(request, 'payments/success.html', context=context)


def CancelView(request):
    context = {
        'title': 'Отмена',
    }
    return render(request, 'payments/cancel.html', context=context)
