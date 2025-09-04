# Tabela do banco de dados de tarefas
from django.db import models
from django.contrib.auth.models import User


class Tarefas(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=2000)
    tipo = models.CharField(max_length=50) 
    data_criado = models.DateTimeField(auto_now_add=True)
    atualizar = models.DateTimeField(auto_now=True)
    concluida = models.BooleanField(default=False)

 
    # Adiciona relação com o usuário e deleta a lista dele caso o usuário seja excluído
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

