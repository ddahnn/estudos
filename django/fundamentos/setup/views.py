from django.shortcuts import render

def home(request):
    nome = "Daniel"
    pessoa = {
        "nome":"Jobervalino",
        "idade":1972,
        "cidade":"Nonoai - RS"
    }
    return render(request, "home.html", {"nome":nome, "pessoa":pessoa})

def about(request):
    frutas = ["maçã", "banana", "laranja", "uva"]

    return render(request, "about.html",{"frutas":frutas})