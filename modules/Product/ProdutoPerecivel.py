from modules.Product.Produto import Produto
from datetime import date
class ProdutoPerecivel ( Produto ):
    def __init__(self, nome, codigo, data_Validade, preco=0, estoque=0, ):
        super().__init__(nome, codigo, preco, estoque)
        self._data_Validade = data_Validade


    @property
    def dataValidade(self):
        return self._data_Validade

