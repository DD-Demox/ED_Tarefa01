class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


class Retangulo:
    def __init__(self, largura, altura, verticePartidaX = 0, verticePartidaY= 0):
        self.altura = altura
        self.largura = largura
        self.verticePartida = Ponto(verticePartidaX, verticePartidaY)

    def acharCentro(self):
        centro = Ponto((self.verticePartida.getX()+self.largura)/2, (self.verticePartida.getY()+self.altura)/2)
        return centro

    def setAltura(self, altura):
        self.altura = altura
        return self.altura

    def setLargura(self, largura):
        self.largura = largura
        return self.largura


r1 = Retangulo(10, 20)
centroR1 = r1.acharCentro()
print(f"{centroR1.getX()} {centroR1.getY()}")

r2 = Retangulo(10,10,5,-34)
centroR2 = r2.acharCentro()
print(f"{centroR2.getX()} {centroR2.getY()}")

