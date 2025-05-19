from modules.Marca import Marca
from modules.Veiculo import Veiculo


class Carro ( Veiculo ) :

    __listaCarros = []
    
    def __init__(self, modelo, cor, marca: Marca, qtdPortas=0, preco=0.0  ):
        super().__init__(modelo, cor, marca, preco)
        self._qtdPortas = qtdPortas

    @property
    def portas(self):
        return self._qtdPortas


    @portas.setter
    def portas(self, quantia):
        if quantia <2:
            return f"A quantia deve ser 2 ou mais portas"
        elif quantia >= 2:
            self._qtd_Portas = quantia
        else: return f"Erro"


    def DefinirPreco(self, novo_preco):
        if novo_preco > 0:
            self.preco = novo_preco

    def cadastrar(self):
        if not all([self.modelo, self.cor, self.marca, self._qtdPortas, self.preco]):
            print("Erro. necessarios todos os dados")
        elif self.preco > 0:
            carro = {
                "Modelo": self.modelo,
                "Cor": self.cor,
                "Marca":self.marca.nome,
                "Quantia Portas": self._qtdPortas,
                "Preço": self.preco
            }
            Carro.__listaCarros.append(carro)
            print(f"O carro {carro}, foi adicionado.")

            
    @classmethod
    def exibirLista(cls):
        print(f"""***  Lista De Carros  ***\n""")
        for  carro in Carro.__listaCarros:
            print(f"{carro}\n")

    def getInfo(self):
        info = super().getInfo()
        return f"{info}" + f"Quantia de protas: {self._qtd_Portas}\n"