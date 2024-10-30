from django.urls import path
from . import views

urlpatterns = [
    path('', views.film_list, name='film_list'),
    path('create/', views.film_create, name='film_create'),
]