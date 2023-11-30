from django.contrib import admin

from catalog.models import Product, Category, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category', 'author', 'publication')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'number', 'name', 'activate')
    list_filter = ('activate',)
