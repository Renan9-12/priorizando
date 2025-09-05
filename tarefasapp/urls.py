from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicialpage, name='inicialpage'),
    path("criar-admin/", views.criar_superuser),

]
