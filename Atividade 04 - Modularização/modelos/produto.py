class Produto:
    def __init__(self, preco=0):
        self._preco = preco

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, valor):
        self._preco = valor