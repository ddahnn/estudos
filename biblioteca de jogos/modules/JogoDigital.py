from modules.Genero import Genero
from modules.Jogo import Jogo

class JogoDigital( Jogo ):
    
    listaJogo = []

    def __init__(self, titulo, plataforma, genero: Genero, tamanho ,preco = 0.0 ):
        super().__init__(titulo, plataforma, genero)
        self.__tamanho = tamanho
        self.preco = preco

    def getInfo(self):
        info = super().getInfo()
        return info + f"Tamanho:   {self.__tamanho} GB."
    
    def cadastrar(self): #type: ignore
        if not all([self.titulo, self.plataforma, self.genero, self.__tamanho ,self.preco]):
            return  "Necessario todos os dados para cadastrar o jogo."
        elif self.preco> 0 :
            jogo = {
                "Titulo": self.titulo,
                "Plataforma":self.plataforma,
                "Genero": self.genero.nome,
                "Midia" : self.__tamanho,
                "Preço" :self.preco
            }
            JogoDigital.listaJogo.append(jogo)
            return f"O jogo {self.titulo}, foi cadastrado com sucesso!"
        
        
    def setPreco(self, novo_preco):
        return super().setPreco(novo_preco)
    

    def ver_Lista(self):
        for digital in JogoDigital.listaJogo:
            print(digital)