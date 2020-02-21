from django.shortcuts import render


def get_menu(request, slug=None):
    return render(request, 'index.html')



