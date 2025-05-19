from modules.Genero import Genero
from abc import ABC, abstractmethod

class Jogo ( ABC ):
    def __init__(self, titulo, plataforma, genero:Genero):
        self.titulo = titulo
        self.plataforma = plataforma
        self.preco = 0
        self.genero = genero


    def getInfo(self):
        return f"""
***  Informações do game ***
Titulo: {self.titulo},
Plataforma: {self.plataforma},
Preco: {self.preco},
Genero: {self.genero.nome}

"""
    def setPreco(self, novo_preco):
        if novo_preco > 0:
            self.preco = novo_preco
        else:
            return f"O preço não pode ser menor que '0'."
        
    @abstractmethod
    def cadastrar(self):
        pass

