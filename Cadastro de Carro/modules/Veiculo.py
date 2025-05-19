from modules.Marca import Marca
from abc import ABC, abstractmethod
class Veiculo ( ABC ) :
    def __init__(self, modelo, cor, marca:Marca , preco = 0.0,) :
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.marca = marca


    @abstractmethod
    def cadastrar(self):
        pass
    
    @abstractmethod 
    def DefinirPreco(self, novo_preco):
        pass

    def getInfo(self):
        return f"""***  Dados Do Veiculo  ***\n
        Modelo: {self.modelo}\n
        Cor: {self.cor}\n
        Preço: {self.preco:.2f}\n
        Marca : {self.marca}\n
"""



