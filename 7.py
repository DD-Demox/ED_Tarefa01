class Tamagochi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 10
        self.idade = 0

    def setNome(self,nome):
        self.nome = nome
        return self.nome

    def setFome(self, fome):
        self.fome = fome
        return self.fome

    def setSaude(self,saude):
        self.saude = saude
        return self.saude

    def setIdade(self, idade):
        self.idade = idade
        return self.idade

    def getNome(self):
        return self.nome

    def getFome(self):
        return self.fome

    def getSaude(self):
        return self.saude

    def getIdade(self):
        return self.idade

    def calcularHumor(self):
        if self.getFome()>=10 or self.getSaude()<=0:
            return "Ta puto!"
        elif self.getFome()>= 7 or self.getSaude()<=3:
            return "Ta irritado"
        elif self.getFome()>= 5 or self.getSaude()<=5:
            return "Ta de boa"
        elif self.getFome()>= 3 or self.getSaude()<=7:
            return "Ta alegre"
        else:
            return "Ta super feliz"


armando = Tamagochi("Armando")
print(armando.calcularHumor())
print(armando.setFome(6))
print(armando.calcularHumor())
print(armando.setSaude(0))
print(armando.calcularHumor())
