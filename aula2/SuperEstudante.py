class Estudante:
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso

    def exibirdados(self):
        print(f'Nome:{self.nome} \n'
              f'Curso:{self.curso}')


class Superior(Estudante):
    def __init__(self, nome, curso, nota_enem):
        super().__init__(nome, curso)
        self.nota_enem = nota_enem


a1 = Estudante('Marquin', 'TSI')
a2 = Superior('Marquin', 'TSI', 615)

a1.exibirdados()
a2.exibirdados()
