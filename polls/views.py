from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

from polls.models import Question

# define um view baseado em função
def index(request):
    # return HttpResponse("Django - Retorno na url -> views Index")
    # return render(request, 'index.html')
    return render(request, 'index.html', {'titulo': 'Últimas Enquetes'})

# define uma view baseada em função
def ola(request):
    # return HttpResponse('Ola Django')
    questions = Question.objects.all()
    context = {'all_questions': questions} # Cria uma variavel context para receber um dicionario
    return render(request,'polls/questions.html', context)

