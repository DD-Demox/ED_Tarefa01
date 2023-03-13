class ContaCorrente:

    def __init__(self, numeroConta, nomeCorrentista, saldo = 0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo

    # alterarNome()
    def setNomeCorrentista(self, novoNome):
        self.nomeCorrentista = novoNome
        return self.nomeCorrentista

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


contaArmando = ContaCorrente(123456, "Arnaldo")
print(contaArmando.setNomeCorrentista("Armando Asch"))
print(contaArmando.saque(100))
print(contaArmando.deposito(12345))
print(contaArmando.saque(100))



