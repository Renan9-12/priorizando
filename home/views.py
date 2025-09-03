from django.shortcuts import render, redirect, get_object_or_404
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
    lista_tarefas = Tarefas.objects.all().order_by('-data_criado')
    return render(request, 'lista_de_tarefas.html', {'tarefas': lista_tarefas})





# Função de adicionar nova tarefa.
@login_required(login_url="/login/")
def add_tarefa(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        tipo = request.POST.get("tipo")



        # Cria e salva no banco.
        Tarefas.objects.create(
            titulo=titulo,
            descricao=descricao,
            tipo=tipo
        )

        # Redireciona para a lista de tarefas.
        return redirect("/home/")

    
    return render(request, "add_tarefa.html")




# Função de editar tarefa
@login_required(login_url="/login/")
def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefas, id=tarefa_id)

    if request.method == "POST":
        # Se veio do botão de excluir
        if "excluir" in request.POST:
            tarefa.delete()
            return redirect("home_page")


        # Se veio do botão de concluir
        if "concluida" in request.POST:
            tarefa.concluida = True   # marca como concluída
            tarefa.save()
            return redirect("home_page")

        # Desmarcar a concluido 
        if "pendente" in request.POST:
            tarefa.concluida = False  # Continua a tarefa
            tarefa.save()
            return redirect("home_page")


        # Caso contrário, é edição normal
        titulo = request.POST.get("titulo")
        descricao = request.POST.get("descricao")
        tipo = request.POST.get("tipo")

        tarefa.titulo = titulo
        tarefa.descricao = descricao
        tarefa.tipo = tipo
        tarefa.save()

        return redirect("home_page")

    return render(request, "editar_tarefa.html", {"tarefa": tarefa})


