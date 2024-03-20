from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

# define um view baseado em função
def index(request):
    return HttpResponse("Hello, World, Pagina Principal. Site de Enquetes")

# define uma view baseada em função
def ola(request):
    return HttpResponse('Ola Django')
