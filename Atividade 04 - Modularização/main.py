from financeiro.vendas import *
from modelos.produto import Produto

opcao = -1
separador = 70*'#'
def menu():
    separador
    print('SELECIONE UMA OPÇÃO')
    while True:
        try:
            opcao = int(input('1 - AVISTA \t 2 - Cartão (vencimento) \t 3 '
                '- Cartão (parcelado) \t 0 -  Sair \t(digite apena o numero):'))
            return opcao
        except(ValueError, BaseException):
            print('ERRO TENTE NOVAMENTE') 
    
def verificarValores():
    while True:
        lista=[]
        try:
            valor = float(input('Digite o valor do produto: '))
            taxa = int(input('Digite a Porcentagem da taxa: '))
            lista.append(valor)
            lista.append(taxa)
            return lista
        except(ValueError, BaseException):
            print('ERRO TENTE NOVAMENTE')

while opcao != 0:
        opcao = menu()
        if (opcao == 0):
            print('TCHAU')
            break
        elif (opcao == 1 or opcao == 2):
            print(separador)
            valores = verificarValores()
            p = Produto(valores[0])
            valorFinal = descontar(p.preco, valores[1])
            print(f'VALOR DO PRODUTO: {p.preco :.2f}R$ \t VALOR DESCONTO:'
                f' {valores[1]}% \t VALOR FINAL: {valorFinal :.2f}R$')
            print(separador)
        elif (opcao == 3):
            print(separador)
            valores = verificarValores()
            p = Produto(valores[0])
            valorFinal = aumentar(p.preco, valores[1])
            print(f'VALOR DO PRODUTO:{p.preco :.2f}R$ \t VALOR DA TAXA: '
                f'{valores[1]}% \t VALOR FINAL: {valorFinal :.2f}R$')
            print(separador)
        else:
            print('DIGITE UMA OPÇÃO VALIDA')
            print(separador)
            