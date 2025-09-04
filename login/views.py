from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required



def logar(request):
    if request.method == "GET":
        return render(request, "login.html") 

    # A função authenticate() é utilizada para receber as informações de login e caso as informações existam, o usuário é autenticado.
    else:
        nome = request.POST.get("nome_logar")
        senha = request.POST.get("senha_logar")

        user = authenticate(username=nome, password=senha)
    

    # Redireciona automaticamente para home/ caso o login der certo.
    if user:
        login(request, user)
        return redirect("/home/")   
   
    else:
        return render(request, "login.html", {"error": "Nome ou senha incorretos."})



#Abraço pra galera da RZ <3