class Funcionario:
    def __init__(self,nome, salario):
        self.nome = nome
        self.salario = salario

    def getNome(self):
        return self.nome

    def setNome(self,novoNome):
        self.nome = novoNome
        return self.nome

    def getSalario(self):
        return self.salario

    def setSalario(self, novoSalario):
        self.salario = novoSalario
        return self.salario

armando = Funcionario("Armando Asch", 3000)
print(armando.getSalario())
print(armando.getNome())

