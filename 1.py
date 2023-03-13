class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    #alteraCor()
    def setCor(self, novaCor):
        self.cor = novaCor

    #mostrarCor()
    def mostraCor(self):
        print(f"A cor da bola é {self.cor}")


bolaArmando = Bola("amarela", 40, "borracha")
bolaArmando.mostraCor()
bolaArmando.setCor("verde")
bolaArmando.mostraCor()
