from abc import ABC, abstractmethod

class Produto(ABC):
    _produtos = []
    __idProduto = 0

    def __init__(self, nome, codigo, preco = 0.0, estoque = 0 ):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.estoque = estoque
        Produto.__idProduto += 1
        self.__id = Produto.__idProduto

        Produto._produtos.append({
            "ID": self.__id,
            "Nome": self.nome,
            "Código": self.codigo,
            "Preço": self.preco,
            "Estoque": self.estoque
        })

    @classmethod
    def repor_estoque(cls, id_produto, nome_produto, quantidade):
        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            return
        for produto in cls._produtos:
            if produto["ID"] == id_produto and produto["Nome"].lower() == nome_produto.lower():
                produto["Estoque"] += quantidade
                print(f"Estoque do produto '{produto['Nome']}' atualizado para {produto['Estoque']}.")
                return
        print("Produto não encontrado. Verifique o ID e o nome.")

    @abstractmethod
    def cadastrarProduto(self):
        pass

    @classmethod
    def venderUnidade(cls, id_produto, nome):
        for produto in cls._produtos:
            if produto["ID"] == id_produto and produto["Nome"].lower() == nome.lower():
                if produto["Estoque"] > 0:
                    produto["Estoque"] -= 1
                    print(f"Estoque do produto '{produto['Nome']}' atualizado para {produto['Estoque']}.")
                else:
                    print("Produto sem estoque.")
                return
        print("Produto não encontrado. Verifique o ID e o nome.")
