class Pokemon:
    def __init__(self, nome):
        self.nome = nome
    def movimenta(self):
        print(f'Eu sou o {self.nome} e estou me movimentando')

class Terra(Pokemon):
    def __init__(self, nome, resistencia):
        super().__init__(nome)
        self.resistencia = resistencia

    def movimenta(self):
        print(f'Eu sou o {self.nome} e estou correndo')

class Voador(Pokemon):
    def movimenta(self):
        print(f'Eu sou o {self.nome} e estou voando')

class Fogo(Pokemon):
    def movimenta(self):
        print(f'Eu sou o {self.nome} e estou atirando fogo')

class Dragao(Voador, Fogo):
    pass

p1 = Pokemon('Arceus')
p2 = Terra('Cubone', 200)
p3 = Dragao('Charizard')
p1.movimenta()
p2.movimenta()
p3.movimenta()