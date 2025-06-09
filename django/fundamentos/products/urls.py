# Importa a função 'path' para definir rotas de URLs no Django
from django.urls import path

# Importa o arquivo views.py do mesmo diretório (o ponto representa o diretório atual)
from . import views






app_name = 'products'

# Lista de URLs da aplicação; define quais rotas serão tratadas e por qual view
urlpatterns = [
    # Define a rota raiz (ex: /) que será tratada pela função 'products_list' da views
    path('', views.products_list, name="list"),
    path('new_product', views.product_new, name='new'),
    path('<slug:slug>', views.product_page, name="page"),
]
