from django import template
from menu.models import Menu

register = template.Library()


@register.inclusion_tag('draw_menu.html')
def draw_menu(name=None, slug=None):
    active = None
    slug = slug if len(slug) > 1 else None

    menu = Menu.objects.prefetch_related('menu_items').get(name=name)
    items = menu.menu_items.all()

    if slug:
        for item in items:
            if item.slug == slug[1:]:
                active = item

    return {'active': active,
            'items': items.exclude(parent__gte=0),
            'counter_nesting_level_from_active': 3
            }


@register.simple_tag
def decrement(value):
    value -= 1
    return value
