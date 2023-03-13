class ContaInvestimento:

    def __init__(self, numeroConta, nomeCorrentista, taxaJuros, saldo=0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo
        self.taxaJuros = taxaJuros

    #alterarNome()
    def setNomeCorrentista(self, novoNome):
        self.nomeCorrentista = novoNome
        return self.nomeCorrentista
    def getSaldo(self):
        return self.saldo

    def deposito(self,quantidade):
        self.saldo = self.saldo + quantidade
        return self.saldo

    def saque(self, quantidade):
        if self.saldo - quantidade < 0:
            print("Saldo nao disponivel")
            return self.saldo
        else:
            self.saldo = self.saldo - quantidade
            return self.saldo

    def adicionaJuros(self):
        self.saldo = round(self.saldo * (1+(self.taxaJuros/100)), 2)


contaArmando = ContaInvestimento("12345","Armando Asch",10,1000)
for i in range(5):
    contaArmando.adicionaJuros()
print(contaArmando.getSaldo())
