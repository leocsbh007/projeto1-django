# importa o modulo de caminhos
from django.urls import path

# importa um modulo intero de views
from polls.views import index, ola

# Cria uma lista de caminhos
urlpatterns = [
    path('index', index, name="index"),
    path('ola', ola, name="ola"),
]