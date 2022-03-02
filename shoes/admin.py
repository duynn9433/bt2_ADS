from django.contrib import admin

from shoes.models import Shoe, Brand


@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'color', 'size', 'brand']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
