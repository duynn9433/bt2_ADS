from django.contrib import admin

# Register your models here.
from laptops.models import Laptop, CPU, RAM


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ['name', 'str_cpu', 'str_ram', 'drive']


@admin.register(CPU)
class CPUAdmin(admin.ModelAdmin):
    list_display = ['model', 'family', 'core', 'thread', 'frequency', 'brand']


@admin.register(RAM)
class RAMAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'bus', 'capacity']
