from django.contrib import admin

from dollshop.models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'category', 'price', 'date_create']
    list_filter = ['category']
