from django.shortcuts import render

from .models import Menu


def my_view(request):
    # Получаем все меню из базы данных
    menus = Menu.objects.prefetch_related('menu_items__parent', 'menu_items__children').select_related('menu_items__menu').all()
    return render(request, 'base.html', {'menus': menus})

def index(request, cat_slug=None):
    return render(request, 'base.html', {'menus': Menu.objects.all()})
