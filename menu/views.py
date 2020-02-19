from django.shortcuts import render
from django.shortcuts import get_list_or_404

from menu.models import Item


def get_menu(request, slug=None):
    return render(request, 'index.html', context={'slug': slug})



