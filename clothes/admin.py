from django.contrib import admin

# Register your models here.
from clothes.models import Vendor, Cloth


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'address']


@admin.register(Cloth)
class ClothAdmin(admin.ModelAdmin):
    list_display = ['color', 'style', 'size', 'str_vendor', 'price']
