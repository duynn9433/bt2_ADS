from django.contrib import admin

# Register your models here.
from mobile_phones.models import MobilePhone, Memory, Producer


@admin.register(MobilePhone)
class MobileAdmin(admin.ModelAdmin):
    list_display = ['name', 'display', 'platform', 'str_memories', 'str_producer']


@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ['ram', 'rom', 'cardSlot']


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
