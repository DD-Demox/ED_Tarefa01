class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def getAltura(self):
        return self.altura

    def envelhecer(self, anosAMais):
        if self.idade >= 21:
            self.idade = self.idade + anosAMais

        elif self.idade + anosAMais >= 20:
           self.altura = self.altura + (abs(self.idade - 20) * 0.005)
           self.idade = self.idade + anosAMais

        else:
            self.altura = self.altura + (anosAMais * 0.005)
            self.idade = self.idade + anosAMais
        return self.idade

    def engordar(self, pesoAMais):
        self.peso = self.peso + pesoAMais
        return self.peso

    def emagrecer(self, pesoAMenos):
        self.peso = self.peso - pesoAMenos
        return self.peso

    def crescer(self, alturaAMais):
        self.altura = self.altura + alturaAMais
        return self.altura



armando = Pessoa("Armando", 32, 94, 1.83)
armandoNovinho = Pessoa("Armando", 5, 30, 1)
print(armando.engordar(4))
print(armando.envelhecer(3))
print(armando.getAltura())
print(armando.crescer(0.01))
print(armandoNovinho.envelhecer(10))
print(armandoNovinho.getAltura())
print(armandoNovinho.envelhecer(5))
print(armandoNovinho.getAltura())
