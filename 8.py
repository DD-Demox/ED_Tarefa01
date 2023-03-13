class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def verBucho(self):
        return self.bucho

    def digerir(self):
        self.bucho = []


macaco1 = Macaco("Armando")
macaco2 = Macaco("Armandinho")

macaco1.comer("Arroz")
print(macaco1.verBucho())
macaco1.comer("Feijao")
print(macaco1.verBucho())
macaco1.digerir()
print(macaco1.verBucho())
macaco1.comer("Sushi")
print(macaco1.verBucho())
print()

macaco2.comer("Feijoada")
print(macaco2.verBucho())
macaco2.comer("Miojo")
print(macaco2.verBucho())
macaco2.comer("Omelete")
print(macaco2.verBucho())

print(macaco2.comer(macaco1))
print(macaco2.verBucho())
