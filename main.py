from modules.personas.Cliente  import  Cliente
from modules.personas.Funcionario  import Funcionario
from modules.Product.Produto import Produto

print("\n" + "*"*20 +f" Cliente "+ "*"*20 + "\n")
c1 = Cliente("Daniel", "000.000.000-00", "dkasjofds")
print(c1.exibirDados())
c1.cadastrar()
print(c1.ver_lista())



print("\n" + "*"*20  + f" Funcionario " + "*"*20 + "\n")
f1 = Funcionario("Alguem", "0000.000.0.00", "234fsdfsf")
f1.cadastrar()
print(f1.exibirDados())
print(f1.ver_lista())


#p1 = Peresivel("Sabão", 5.0, 10)
#p2 = Peresivel("Shampoo", 12.5, 5)
'''
Produto.repor_estoque(1, "Sabão", 5)      # Ok
Produto.repor_estoque(2, "shampoo", 10)   # Ok (case insensitive)
Produto.repor_estoque(3, "Condicionador", 5)  # Produto não encontrado
Produto.repor_estoque(1, "Sabão", -3)     # Quantidade inválida
'''