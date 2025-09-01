from django.shortcuts import render

# Create your views here.



#pagina inicial do site
def logar(request):
    return render(request, 'login.html', {})


