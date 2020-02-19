from django import template
from django.urls import reverse
from menu.models import Item

register = template.Library()


@register.inclusion_tag('draw_menu.html')
def draw_menu(slug=None):
    active = None
    items = Item.objects.select_related('parent')
    if slug:
        active = Item.objects.get(slug=slug)
    return {
        'active': active,
        'items': items.exclude(parent__gte=0),
        'counter_nesting_level_from_active': 3
    }


@register.simple_tag
def decrement(value):
    value -= 1
    return value
