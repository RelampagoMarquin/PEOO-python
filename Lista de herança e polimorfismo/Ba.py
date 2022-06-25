class Conta_Corrente():
    def __init__(self, agencia, numero_da_conta, saldo):
        self.agencia = agencia
        self.numero_da_conta = numero_da_conta
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


class ContaPF(Conta_Corrente):
    def __init__(self, agencia, numero_da_conta, saldo, Cpf, Renda_mensal):
        super() .__init__(agencia, numero_da_conta, saldo)
        self.cpf = Cpf
        self.renda = Renda_mensal

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


class ContaPJ(Conta_Corrente):
    def __init__(self, agencia, numero_da_conta, saldo, Cnpj, Capital_investido):
        super() .__init__(agencia, numero_da_conta, saldo)
        self.cnpj = Cnpj
        self.capital = Capital_investido

    def sacar(self, valor_sacado):
        saldoaux = self.saldo
        capaux= self.capital
        status = ''
        if valor_sacado <= self.saldo:
            self.saldo -= valor_sacado
            status = 'Autorizado'
        elif valor_sacado > self.saldo and self.capital > valor_sacado:
            status = 'Autorizado'
            if self.saldo < valor_sacado:
                vd=valor_sacado-self.saldo
                self.saldo=0
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

pf = ContaPF(1, '45-1', 500, '684.276.460-20', 7000)
pj = ContaPJ(1, '1111-1', 500, '46.031.672/0001-65', 1000)
pj.sacar(600)
pf.sacar(600)
pj.depositar(1500)
pj.depositar(100,pf)
pf.depositar(500)
pf.depositar(1000,pj)

