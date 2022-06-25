class ContaCorrente:
    def __init__(self, agencia, numConta, saldo):
        self.agencia = agencia
        self.numConta = numConta
        self.saldo = saldo

    def sacar(self):
        pass

    def depositar(self, deposito, outraconta=-1):
        print('===========================================================\n')
        if(outraconta != -1):
            outraconta.saldo += deposito
            print(f'Valor depositado:{deposito}\n'
                  f'Saldo atual:{outraconta.saldo}\n')
        else:
            self.saldo += deposito
            print(f'Valor depositado:{deposito}\n'
                  f'Saldo é atual:{self.saldo}\n')


class ContaPJ(ContaCorrente):
    def __init__(self, agencia, numConta, saldo, cnpj, capital):
        super().__init__(agencia, numConta, saldo)
        self.cnpj = cnpj
        self.capital = capital

    def visualizar(self):
        print('===============================================================\n'
              f'Agencia:{self.agencia}\nNumero da Conta:{self.agencia}\n'
              f'Saldo:{self.saldo}\nCNPJ:{self.cnpj}\nCapital:{self.capital} \n'
              '===============================================================')

    def sacar(self, valor_sacado):
        saldoaux = self.saldo
        capaux = self.capital
        status = ''
        if valor_sacado <= self.saldo:
            self.saldo -= valor_sacado
            status = 'Autorizado'
        elif valor_sacado > self.saldo and self.capital > valor_sacado:
            status = 'Autorizado'
            if self.saldo < valor_sacado:
                vd = valor_sacado-self.saldo
                self.saldo = 0
                self.capital -= vd
            else:
                self.saldo -= valor_sacado
        else:
            status = 'Não Autorizado'
        print('===========================================================\n'
              'Tipo de conta: Conta Juridica\n'
              f'Saldo da conta:{saldoaux}| Saque:{valor_sacado}| Capital investido:{capaux}'
              f'Status do saque: {status}\n'
              f'Saldo da conta = {self.saldo}\n'
              f'Saldo do Capital investido:{self.capital}\n')


class ContaPF(ContaCorrente):
    def __init__(self, agencia, numConta, saldo, cpf, renda):
        super().__init__(agencia, numConta, saldo)
        self.cpf = cpf
        self.renda = renda

    def visualizar(self):
        print('=============================================================== \n'
              f'Agencia:{self.agencia}\nNumero da Conta:{self.agencia}\n'
              f'Saldo:{self.saldo}\nCPF:{self.cpf}\nRenda:{self.renda}\n'
              '===============================================================')

    def sacar(self, valor_sacado):
        saldoaux = self.saldo
        status = ''
        if valor_sacado >= self.saldo + 800 and self.renda > 5000:
            self.saldo -= valor_sacado
            status = 'Autorizado'
        elif valor_sacado > self.saldo and self.renda > 5000:
            status = 'Não Autorizado'
        else:
            self.saldo -= valor_sacado
            status = 'Autorizado'
        print('===========================================================\n'
              'Tipo de conta: Conta Física\n'
              f'Saldo da conta:{saldoaux}| Saque:{valor_sacado}| Renda:{self.renda}'
              f'Status do saque: {status}\n'
              f'Saldo da conta = {self.saldo}\n')


pf = ContaPF(1, '45-1', 500, '684.276.460-20', 7000)
pj = ContaPJ(1, '1111-1', 500, '46.031.672/0001-65', 1000)
pj.sacar(600)
pf.sacar(600)
pj.depositar(1500)
pj.depositar(100,pf)
pf.depositar(500)
pf.depositar(1000,pj)

