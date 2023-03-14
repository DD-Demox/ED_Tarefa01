import random


class Tamagochi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0,10)
        self.saude = random.randint(0,10)
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

class Fazenda:
    def __init__(self, nome):
        self.fazenda=[]
        self.nome = nome

    def getNome(self):
        return self.nome

    def adicionarTamagochi(self,tamagochi):
        self.fazenda.append(tamagochi)

    def alimentarTodos(self, tempo):
        for t in self.fazenda:
            t.alimentar(tempo)
            print(t.calcularHumor())

    def cuidarTodos(self, tempo):
        for t in self.fazenda:
            t.cuidarSaude(tempo)
            print(t.calcularHumor())

    def statusTodos(self):
        for t in self.fazenda:
            t.secreto()



jogo = True
print("Bem vindo ao jogo da Fazenda")
nomeFazenda = input("Digite o nome da sua Fazenda: ")
fazenda = Fazenda(nomeFazenda)

while jogo:
    print(f'Fazenda {fazenda.getNome()}')
    print("O que quer fazer?")
    print("1 - Novo Tamagochi")
    print("2 - Alimentar todos")
    print("3 - Cuidar de todos")
    print("10 - Sair")
    try:
        escolha = int(input())
        if escolha == 1:
            nome = input("Digite o nome do Tamagochi ")
            tamagochi = Tamagochi(nome)
            fazenda.adicionarTamagochi(tamagochi)
        elif escolha == 2:
            tempo = int(input("Digite o tempo"))
            fazenda.alimentarTodos(tempo)
        elif escolha == 3:
            tempo = int(input("Digite o tempo"))
            fazenda.cuidarTodos(tempo)
        elif escolha == 98:
            for t in fazenda.fazenda:
                print(t)
        elif escolha == 99:
            fazenda.statusTodos()
        elif escolha == 10:
            jogo = False
        else:
            print("Escolha invalida")
    except ValueError:
        print("Escolha invalida")

