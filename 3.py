class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def setLadoA(self,ladoA):
        self.ladoA = ladoA

    def setLadoB(self,ladoB):
        self.ladoB=ladoB

    def getLadoA(self):
        return self.ladoA

    def getLadoB(self):
        return self.ladoB

    def calcularArea(self):
        return self.ladoA * self.ladoB

    def calcularPerimetro(self):
        return (self.ladoA*2)+(self.ladoB * 2)

print("Digite as medidas da sala")
ladoASala = float(input("Lado A da sala: "))
ladoBSala = float(input("Lado B da sala: "))
sala = Retangulo(ladoASala, ladoBSala)
print("Digite as medidas dos ladrilhos")
ladoALadrilho = float(input("Lado A do ladrilho: "))
ladoBLadrilho = float(input("Lado B do ladrilho: "))
ladrilho = Retangulo(ladoALadrilho, ladoBLadrilho)

quantidadeLadrilho = sala.calcularArea()/ladrilho.calcularArea()
rodape = sala.calcularPerimetro()

print(f"Você precisará de {quantidadeLadrilho} de ladrilhos e {rodape} de rodape ")




