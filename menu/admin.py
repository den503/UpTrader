from django.contrib import admin
from menu.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name', )}
