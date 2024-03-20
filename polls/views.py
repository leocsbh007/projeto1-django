from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

# define um view baseado em função
def index(request):
    # return HttpResponse("Django - Retorno na url -> views Index")
    return render(request, 'index.html')

# define uma view baseada em função
def ola(request):
    return HttpResponse('Ola Django')
