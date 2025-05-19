from modules.Genero import Genero
from modules.Jogo import Jogo



class JogoFisico( Jogo ) :
 
    jogoLista = []

    def __init__(self, titulo, plataforma, genero: Genero, midia, preco = 0):
        super().__init__(titulo, plataforma, genero)
        self._midia = midia
        self.preco = preco

    def cadastrar(self): #type: ignore
        if not all([self.titulo, self.plataforma, self.genero, self._midia ,self.preco]):
            return  "Necessario todos os dados para cadastrar o jogo."
        elif self.preco> 0 :
            jogo = {
                "Titulo": self.titulo,
                "Plataforma":self.plataforma,
                "Genero": self.genero.nome,
                "Midia" : self._midia,
                "Preço" :self.preco
            }
            JogoFisico.jogoLista.append(jogo)
            return f"O jogo {self.titulo}, foi cadastrado com sucesso!"

    def setPreco(self, novo_preco):
        return super().setPreco(novo_preco)
    

    def getInfo(self):
        info = super().getInfo()
        return info + f"Midia:  {self._midia}"
    
    def ver_Lista(self):
        for jogos in JogoFisico.jogoLista:
            print(jogos)


