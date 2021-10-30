from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola Mundo!! Esta es la raiz de la aplicación de agenda.")
