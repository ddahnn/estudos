

class Marca:
    __Id = 0
    def __init__(self, nome):
        Marca.__Id +=1
        self._id = Marca.__Id
        self.nome = nome
    
    def __str__(self):
        return f"{self.nome}"
    
    @property
    def id(self):
        return self._id
    

