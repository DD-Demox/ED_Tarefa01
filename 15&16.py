import random


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
        if self.getFome() >= 10 or self.getSaude() <= 0:
            return f"{self.nome} ta puto!"
        elif self.getFome() >= 7 or self.getSaude() <= 3:
            return f"{self.nome} ta irritado"
        elif self.getFome() >= 5 or self.getSaude() <= 5:
            return f"{self.nome} ta de boa"
        elif self.getFome() >= 3 or self.getSaude() <= 7:
            return f"{self.nome} ta alegre"
        else:
            return f"{self.nome} ta super feliz"

    def passarTempo(self, tempo,alimentou, saude):
        self.idade = self.idade + tempo
        if not alimentou:
            self.fome = self.fome + tempo
        aleatorio = random.randint(1,10)
        if (aleatorio == 1 or aleatorio == 2) and not saude:
            self.saude = self.saude - tempo


    def cuidarSaude(self, tempo):
        self.passarTempo(tempo, False, True)
        self.saude = self.saude + tempo

    def alimentar(self,tempo):
        self.passarTempo(tempo, True, False)
        self.fome = self.fome - tempo

    def secreto(self):
        print(f"Nome: {self.getNome()}")
        print(f"Idade: {self.getIdade()}")
        print(f"Saude: {self.getSaude()}")
        print(f"Fome: {self.getFome()}")

print("Bem vindo ao tamagochi")
nome = input("Digite o nome do seu tamagochi: ")
tamagochi = Tamagochi(nome)
jogo = True

while jogo:
    print(f"O que voce quer fazer com o {tamagochi.getNome()}")
    print("1 - alimentar ")
    print("2 - cuidar da saude")
    print("3 - passar tempo")
    print("4 - Sair")
    try:
        escolha = int(input())
        if escolha == 1:
            tempo = int(input("Por quanto tempo? "))
            tamagochi.alimentar(tempo)
            print(tamagochi.calcularHumor())
        elif escolha == 2:
            tempo = int(input("Por quanto tempo? "))
            tamagochi.cuidarSaude(tempo)
            print(tamagochi.calcularHumor())
        elif escolha == 3:
            tempo = int(input("Por quanto tempo? "))
            tamagochi.passarTempo(tempo, False, False)
            print(tamagochi.calcularHumor())
        elif escolha == 4:
            jogo = False
        elif escolha == 99:
            tamagochi.secreto()
        else:
            print("Escolha invalida")
    except ValueError:
        print("Escolha invalida")

print("Fim do jogo")









