from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def domingo(requset):
    return HttpResponse('Ler um livro sobre DJango')


def segunda(request):
    return HttpResponse("Assistir Breaking Bad")

def terca(request):
    return HttpResponse("Estudar programação python.")
