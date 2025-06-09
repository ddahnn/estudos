from django.db import models  # Importa os recursos de modelagem do Django (Model, CharField, etc.)

# Define uma classe 'Products' que representa um produto no banco de dados
class Products(models.Model):
    # Campo de texto com no máximo 100 caracteres para o nome do produto
    name = models.CharField(max_length=100)  
    
    # Campo de texto longo para a descrição do produto
    description = models.TextField()
    
    # Campo numérico para o preço, com até 10 dígitos no total e 2 casas decimais
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Campo para armazenar a quantidade em estoque; só aceita números positivos
    stock = models.PositiveIntegerField()
    
    # Campo para o 'slug', geralmente usado em URLs (ex: produto-exemplo)
    slog = models.SlugField()  

    banner = models.ImageField(blank=True)
    
    # Armazena automaticamente a data e hora em que o produto foi criado
    creat_at = models.DateTimeField(auto_now_add=True)

    # Define como o objeto será exibido como string (ex: no painel admin)
    def __str__(self) -> str:
        return self.name
