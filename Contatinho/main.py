from modelo.Contato import *
c = Contato()
def salvarContato(c):
    arquivo = open("contatos.txt", 'a+', encoding='utf-8')
    arquivo.write(f'Nome: {c.nome} \t Telefone: {c.telefone} \t email: {c.email}\n' )
    arquivo.close()
    return 'Contato salvo com sucesso'

def visualizarContatos():
    arquivo = open("contatos.txt", 'r', encoding='utf-8')
    print(arquivo.read())
    arquivo.close()

def menu():
    print('################# MENU #################\n'
          '1 - Listar Contato\n'
          '2 - Adicionar Contato\n'
          '3 - SAIR\n')
    try:
        opcao = int(input('Escolha uma opção (Digite o numero):'))
        return opcao
    except ValueError:
        print('Parece que você digitou uma letra, DIGITE SOMENTE NUMERO!!!')
    except BaseException:
        print('EITA VOCÊ CAIU NO ERRO GENERICO')

opcao = -1
while opcao != 3:
    opcao = menu()
    if(opcao == 1):
        visualizarContatos()
    elif(opcao == 2):
        c.nome = str(input('DIGITE O NOME DO CONTATO(deixe em branco se não tiver): '))
        c.telefone = str(input(('DIGITE O NUMERO DO TELEFONE(deixe em branco se não tiver): ')))
        c.email = str(input(('DIGITE O EMAIL (deixe em branco se não tiver): ')))
        print (salvarContato(c))
    else:
        print('OPÇÂO INVALIDA')