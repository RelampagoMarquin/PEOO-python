from geometria import *
import * from geometria
class FormaGeometrica:
    def __init__(self):
        self._area = 0

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, area):
        self._area = area



class Tringulo(FormaGeometrica):
    def __init__(self, base, altura):
        super().__init__()
        self._base = base
        self._altura = altura

    @property
    def base(self):
        return self._base

    @property
    def altura(self):
        return self._altura


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        super().__init__()
        self._raio = raio
        self._pi = 3.14

    @property
    def raio(self):
        return self._raio

    @property
    def pi(self):
        return self._pi


class Trapezio(FormaGeometrica):
    def __init__(self, bMaior, bMenor, altura):
        super().__init__()
        self._bMaior = bMaior
        self._bMenor = bMenor
        self._altura = altura

    @property
    def bMaior(self):
        return self._bMaior

    @property
    def bMenor(self):
        return self._bMenor

    @property
    def altura(self):
        return self._altura

cir = Circulo(10)
print(circulo.areaC(cir))
tri = Tringulo(10, 5)
print(t)
