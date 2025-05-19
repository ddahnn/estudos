from modules.Marca import Marca
from modules.Veiculo import Veiculo


class Moto ( Veiculo ) :

    __listaMotos = []
    
    def __init__(self, modelo, cor, marca: Marca, cilindradas=0, preco=0.0  ):
        super().__init__(modelo, cor, marca, preco)
        self.__cilindradas = cilindradas

    @property
    def cilindrada(self):
        return self.__cilindradas


    @cilindrada.setter
    def cilindrada(self, cilindradas):
        if cilindradas > 2 :
            self.__cilindradas = cilindradas
            return f"Cilindradas alteradas"


    def DefinirPreco(self, novo_preco):
        if novo_preco > 0:
            self.preco = novo_preco

    def cadastrar(self):
        if not all([self.modelo, self.cor, self.marca, self.__cilindradas, self.preco]):
            print("Erro. necessarios todos os dados")
        elif self.preco > 0:
            moto = {
                "Modelo": self.modelo,
                "Cor": self.cor,
                "Marca":self.marca.nome,
                "Cilindrada": self.__cilindradas,
                "Preço": self.preco
            }
            Moto.__listaMotos.append(moto)
            print(f"O carro {moto}, foi adicionado.")
    
    @classmethod
    def exibirLista( cls ):
        print(f"""***  Lista De Carros  ***\n""")
        for  moto in Moto.__listaMotos:
            print(f"{moto}\n")

    def getInfo(self):
        info = super().getInfo()
        return info + f"Cilindradas: {self.__cilindradas}\n"
    

