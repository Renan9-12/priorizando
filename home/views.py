from django.shortcuts import render

# Create your views here.



#pagina inicial do site
def homepage(request):
    return render(request, 'home.html', {})


