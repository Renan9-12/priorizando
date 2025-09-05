from django.shortcuts import render

# Create your views here.



#pagina inicial do site
def inicialpage(request):
    return render(request, 'inicio.html', {})


# Tudo começa aqui

from django.http import HttpResponse
from django.contrib.auth.models import User

def criar_superuser(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "pablorenan1946@gmail.com", "pablo1234renan")
        return HttpResponse("Superuser criado!")
    return HttpResponse("Superuser já existe!")
