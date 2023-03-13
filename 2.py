class Quadrado:
    def __init__(self, tamanhoLado):
        self.tamanhoLado = tamanhoLado

    def setTamanhoLado(self, novoLado):
        self.tamanhoLado = novoLado

    def getTamanhoLado(self):
        return self.tamanhoLado

    def calcularArea(self):
        return self.tamanhoLado * self.tamanhoLado


quadradoArmando = Quadrado(4)
print(f"O lado tem tamanho {quadradoArmando.getTamanhoLado()}")
quadradoArmando.setTamanhoLado(5)
print(f"O lado tem tamanho {quadradoArmando.getTamanhoLado()}")
print(f"A area do quadrado é de {quadradoArmando.calcularArea()}")
