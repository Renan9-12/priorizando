from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate



def registrar(request):
    if request.method == "GET":
        return render(request, "register.html")
    

    # Recebe as informações de registro e verifica se já existe usuário com o mesmo já existe usuário com o mesmo username.
    else:
        username = request.POST.get("nome_inserido")
        email = request.POST.get("email_inserido")
        senha = request.POST.get("senha_inserida")
   
        user = User.objects.filter(username__iexact=username).first()


        if user:
            return render(request, "register.html", {"error": "Usuário já existe!"})
            print("usuário ja existe")

        # Se o nome de usuário não estiver cadastrado, o novo usuário é registrado com sucesso.
        else:
            novo_usuario = User.objects.create_user(username=username, email=email, password=senha)
            novo_usuario.save()
            print("Registrando usuário:", username, email)

            # o usuário é autenticado automaticamente e direcionado para o home/
            user_auth = authenticate(username=username, password=senha)
            if user_auth:
                login(request, user_auth)
                return redirect("/home/")

            return render(request, "register.html", {"error": "Erro ao autenticar novo usuário."})




# Me socorre nessa função, Deus!!
# Atualização: Deu certo, Obrigado meu Deus!!!
