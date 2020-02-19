from django.shortcuts import render
from django.shortcuts import get_list_or_404

from menu.models import Item


def get_menu(request, slug=None):
    item = None
    items = Item.objects.select_related('child')
    if slug:
        item = Item.objects.get(slug=slug)

    template_name = 'index.html'
    context = {
        'item': item,
        'items': items.exclude(parent__gte=0),
    }
    return render(request, template_name, context)
