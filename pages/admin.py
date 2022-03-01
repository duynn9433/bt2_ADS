from django.contrib import admin

# Register your models here.
from pages.models import Pages


@admin.register(Pages)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'permalink']
