class Calcnotas:
    def __init__(self, nome, n1, n2, n3, n4):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.media = 0
        self.situacao = ''
    
    def aprovado(self):
        self.media = (self.n1 * 2 + self.n2 * 2 + self.n3 * 3 + self.n4 * 3)/10
        if(self.media > 60):
            self.situacao = 'APROVADO'
        else:
            self.situacao = 'REPROVADO'
alunos=[]
a1 = Calcnotas('John', 100, 70, 80, 30)
alunos.append(a1)
a2 = Calcnotas('Undertaker', 50, 60, 100, 100)
alunos.append(a2)
for aluno in alunos:
    aluno.aprovado()
    print(f'Nome:{aluno.nome} \n Notas: \n B1:{aluno.n1} \n B2:{aluno.n2} \n B3:{aluno.n3} \n B4:{aluno.n4} \n MEDIA:{aluno.media} \n Situação:{aluno.situacao}')
    print('=================================================================================')