from modules.Marca import Marca
from modules.Carro import Carro
from modules.Moto import Moto

m = Marca("honda")

c1 = Carro("Fit", "Branco", m ,4, 75000.00)

c1.cadastrar()
print("")
print(c1.exibirLista())


print("Moto")
mm1 = Marca("Honda")
m1 = Moto("Strada", "Roxa", mm1, 200, 4000.00)

m1.cadastrar()

print(m1.exibirLista())