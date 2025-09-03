from django.shortcuts import render
from .models import Tarefas
from django.contrib.auth.decorators import login_required


#pagina principal do site


# Na linha abaixo tem a função que só deixa o usuário acessar o home se estiver logado.
@login_required(login_url="/login/")
def home_page(request):


    # Debug da sessão e usuário
    print(">>> Usuário atual:", request.user)   # Mostra o usuário logado
    print(">>> Autenticado?", request.user.is_authenticated)   # True ou False


    # Lista todas as tarefas pela ordem que elas foram adicionadas.
    lista_tarefas = Tarefas.objects.all().order_by('-prazo')
    return render(request, 'lista_de_tarefas.html', {'tarefas': lista_tarefas})


@login_required(login_url="/login/")
def add_tarefa(request):
    if request.method == "GET":
        return render(request, 'add_tarefa.html')
