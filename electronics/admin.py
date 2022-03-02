from django.contrib import admin

from electronics.models import Electronic, Size


@admin.register(Electronic)
class ElectronicAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'wattage', 'size', 'brand']


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['width', 'height', 'deep', 'weight']