import random

separador = 30*'#'
class Jogador:
    def __init__(self, nome, numero, posicao, qualidade=0, cartoes=0):
        self._nome = nome
        self._numero = numero
        self._posicao = posicao
        self._qualidade = qualidade
        self._cartoes = cartoes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def posicao(self):
        return self._nome

    @posicao.setter
    def posicao(self, posicao):
        self._posicao = posicao

    @property
    def qualidade(self):
        return self._qualidade

    @qualidade.setter
    def qualidade(self, qualidade):
        try:
            if qualidade < 100:
                if(qualidade > 0):
                    self._qualidade = qualidade
                else:
                    self._qualidade = 0
            else:
                self._qualidade = 100
        except (ValueError, BaseException):
            print('APENAS NUMEROS SÃO VALIDOS')

    @property
    def cartoes(self):
        return self._cartoes

    @cartoes.setter
    def cartoes(self, cartoes):
        try:
            self._cartoes = cartoes
        except (ValueError, BaseException):
            print('APENAS NUMEROS SÃO VALIDOS')

    def sofre_lesao(self):
        lesionado = self.qualidade * (1 - (random.randint(5, 40) / 100))
        self.qualidade = lesionado

    def treinamento(self):
        lesionado = self.qualidade * (1 + (random.randint(5, 40) / 100))
        self.qualidade = lesionado

    def status_jogador(self):
        print(f'NOME: {self.nome}\nQUALIDADE: {self.qualidade}\nQUANTIDADE DE CARTOES: {self.cartoes}\n{separador}')


def aplicar_cartoes(jogador, qtd):
    cartoes = jogador.cartoes + qtd
    jogador.cartoes = cartoes


