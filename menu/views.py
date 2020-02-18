from django.shortcuts import render
from django.shortcuts import get_list_or_404

from menu.models import Item


def get_menu(request, slug=None):
    item = None
    items = Item.objects.prefetch_related('child').all()
    if slug:
        item = Item.objects.get(slug=slug)

    template_name = 'index.html'
    context = {
        # 'item': item,
        'items': items,
    }
    return render(request, template_name, context)
