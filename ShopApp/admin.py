from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_html_photo', 'available', 'updated')
    list_display_links = ('id', 'name')
    list_editable = ('available',)
    search_fields = ('name', 'description')
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ('available', 'created')
    fields = ('name', 'slug', 'category', 'description', 'image', 'get_html_photo', 'available')
    readonly_fields = ('created', 'updated', 'get_html_photo')

    save_on_top = True

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50 height=50")

    get_html_photo.short_description = 'Фото'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.site_title = admin.site.site_header = 'Админ-панель интернет магазина'
