from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

"""
Имеется две модели - Category и Product.
В модели Product мы задаем цену, название, изображение и т.д.
Category нужна для того, чтобы связать определенный продукт с определенной категорией
"""


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('shop:category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование товара')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение товара')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость (в рублях)')
    stock = models.PositiveIntegerField(verbose_name='Количество товара')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создание позиции')
    updated = models.DateTimeField(auto_now=True, verbose_name='Последнее время изменения позиции')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Позиции товаров'
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('shop:product', kwargs={'product_slug': self.slug})

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
