from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('adicionar_tarefa/', views.add_tarefa, name='add_tarefa'),
    path("editar/<int:tarefa_id>/", views.editar_tarefa, name="editar_tarefa"),
    path('logout/', views.deslogar, name="logout"),
]
