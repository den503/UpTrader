"""
menu URL Configuration
"""
from django.urls import path

from menu.views import get_menu

app_name = 'menu'

urlpatterns = [
    path("", get_menu, name="get_menu"),
    path("/<str:slug>", get_menu, name="get_menu"),
]