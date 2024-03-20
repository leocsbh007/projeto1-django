from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

# define um view baseado em função
def index(request):
    # return HttpResponse("Django - Retorno na url -> views Index")
    # return render(request, 'index.html')
    return render(request, 'index.html', {'titulo': 'Últimas Enquetes'})

# define uma view baseada em função
def ola(request):
    return HttpResponse('Ola Django')
