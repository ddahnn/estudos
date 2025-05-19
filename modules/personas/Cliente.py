from modules.personas.Pessoa import Pessoa

class Cliente( Pessoa ) :
    __listaCliente = []
    __idCliente = 0
    def __init__(self, nome, cpf, endereco):
        super().__init__(nome, cpf, endereco)
        Cliente.__idCliente += 1
        self.__id = Cliente.__idCliente 

    def cadastrar(self):
        if not all([self.nome, self._cpf, self.endereco]):
            print('Necessario todos os dados Para efetuar o cadastro.')
        elif self._cpf in Cliente.__listaCliente:
            print(f"O cliente já esta cadastrado")
        else:
            pessoa={
                "ID Cliente" : self.__id,
                "Nome": self.nome,
                "CPF": self._cpf,
                "Endereço": self.endereco
            }
            Cliente.__listaCliente.append(pessoa)
            print(f"O Cliente  {pessoa['Nome']}, foi adicionado.")

    @classmethod
    def  ver_lista( cls ):
        for cliente in Cliente.__listaCliente:
            return   f"""
    ***   Lista de cadastro   ***
    \n{cliente}
    """
    
    def exibirDados(self):
        info= super().exibirDados()
        return info + f"ID Cliente : {self.__id}"

