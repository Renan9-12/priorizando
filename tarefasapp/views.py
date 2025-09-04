from django.shortcuts import render

# Create your views here.



#pagina inicial do site
def inicialpage(request):
    return render(request, 'inicio.html', {})


# Tudo começa aqui