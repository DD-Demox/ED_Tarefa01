class Carro:
    def __init__(self,quantidadeKmLitro):
        self.quantidadeKmLitro = quantidadeKmLitro
        self.quantidadeCombustivel = 0

    #obterGasolina()
    def getQuantidadeCombustivel(self):
        return self.quantidadeCombustivel

    def adicionarGasolina(self,quantidadeAdicionada):
        self.quantidadeCombustivel = self.quantidadeCombustivel + quantidadeAdicionada

    def andar(self,kmAndado):
        if kmAndado > self.quantidadeCombustivel*self.quantidadeKmLitro:
            print(f"Nao tinha combustivel suficiente para andar tudo isso, so andou {self.quantidadeCombustivel*self.quantidadeKmLitro} Km")
            self.quantidadeCombustivel = 0
        else:
            self.quantidadeCombustivel = self.quantidadeCombustivel - kmAndado/self.quantidadeKmLitro

fusca = Carro(15)
fusca.adicionarGasolina(20)
fusca.andar(3000)
print(fusca.getQuantidadeCombustivel())
fusca.adicionarGasolina(30000)
fusca.andar(3000)
print(fusca.getQuantidadeCombustivel())