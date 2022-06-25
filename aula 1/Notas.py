class CalcNotas:

    """Construtor - constroi o objeto"""
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
        self.media = 0
        self.situacao = ''
        self.matriculado = "MATRICULADO"

    """Calcula a media"""
    def calc(self):
        """metodo split divide a string"""
        ns = input('Digite as notas: ').split()
        self.notas = [int(n) for n in ns]
        self.media = sum(self.notas) / len(self.notas)
        print(self.notas)
        print(self.media)

    """metodo para calcular media e situação"""
    def status(self):
        if self.media > 60:
            self.situacao = 'APROVADO'
        else:
            self.situacao = 'REPROVADO'

    """Metodo de cancelar matricula"""
    def cancelar(self):
        self.matriculado = "MATRICULA CANCELADA"
        return f'A matricula do aluno {self.nome} está cancelada.'


alunos = []
"""criação de um objeto"""
a1 = CalcNotas("John")
a1.calc()
"""
a1 = CalcNotas('John', 100, 70, 80, 30)
alunos.append(a1)
a2 = CalcNotas('Undertaker', 50, 60, 100, 100)
alunos.append(a2)
a3 = CalcNotas('Roman', 50, 60, 10, 50)
alunos.append(a3)
a4 = CalcNotas('Julio', 30, 60, 45, 30)
a4.cancelar()
alunos.append(a4)
"""
"""Print
for aluno in alunos:
    aluno.status()
    print(f'Nome:{aluno.nome} \n Notas: \n B1:{aluno.n1} \n '
          f'B2:{aluno.n2} \n B3:{aluno.n3} \n B4:{aluno.n4} \n '
          f'MEDIA:{aluno.media} \n Situação:{aluno.situacao} \n '
          f'{aluno.matriculado}')
    print(30*'=')
"""
