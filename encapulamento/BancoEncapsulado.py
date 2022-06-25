class Conta:
    """
    o _ é uma formatação permite a modificação
    o __ Deixa o arquivo privado
    """
    def __init__(self, saldo, cliente):
        self._saldo = saldo
        self._cliente = cliente

# praticamente o getter

    @property
    def nome(self):
        return self._cliente

# o property criado retorna o nome e encpsula a variavel
    @nome.setter
    def nome(self, nome):
        self.nome = nome

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, novosaldo):
        if novosaldo < 0:
            print('NEGATIVO NÃO')
        else:
            self.saldo = novosaldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def extrato(self):
        print(f'Saldo:{self.saldo}')


c1 = Conta(1000, 'Marcos')
c2 = Conta(500, 'Matheus')
c2.saldo = 600
#não é necessario usar parenteses, pois é tratado como um atributo
print(f'{c2.saldo}')
# para acessar é necessario usar a
# c1._Conta__saldo = 1000
