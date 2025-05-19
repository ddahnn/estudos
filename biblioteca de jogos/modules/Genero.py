class Genero:
    _autoId = 0
    def __init__(self, nome):
        Genero._autoId +=1
        self.id =Genero._autoId
        self.nome = nome

    def __str__(self):
        return f"{self.nome}"