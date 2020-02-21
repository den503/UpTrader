from django.contrib import admin
from menu.models import Item, Menu


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name']
