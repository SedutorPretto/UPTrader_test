from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_menu'),
    path('<slug:cat_slug>/', views.index, name='draw_menu')
]