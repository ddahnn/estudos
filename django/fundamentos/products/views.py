# Importa a função 'render', usada para renderizar templates HTML com contexto
from django.shortcuts import render
from .models import Products
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Aqui começam as views da aplicação
# Define a função 'products_list', que será chamada quando o usuário acessar a rota correspondente
def products_list(request):
    # Retorna uma resposta renderizando o template 'products/products.html'
    # O primeiro argumento é o objeto 'request', o segundo é o caminho para o template
    product = Products.objects.all().order_by("creat_at")
    return render(request, 'products/products.html',{"products": product})

def product_page(request, slug):
    product = Products.objects.get(slog=slug)
    return render(request, 'products/product_page.html',{'product':product})

@login_required(login_url = '/users/login')
def product_new(request):
    return render(request, 'products/product_new.html')