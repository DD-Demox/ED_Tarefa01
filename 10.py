class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel = 0):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    #alteraQuantidadeCombustivel()
    def setQuantidadeCombustivel(self,valor):
        self.quantidadeCombustivel = valor
        return self.quantidadeCombustivel

    def getQuantidadeCombustivel(self):
        return self.quantidadeCombustivel

    #alteraValor()
    def setValorLitro(self, novoValor):
        self.valorLitro = novoValor
        return self.valorLitro

    #alteraCombustivel()
    def setTipoCombustivel(self,novoTipo):
        self.tipoCombustivel = novoTipo
        return self.tipoCombustivel

    def verificarQuantidadeDisponivel(self, quantidadeRetirada):
        if self.getQuantidadeCombustivel() - quantidadeRetirada < 0:
            return False
        else:
            return True

    def abastecerPorValor(self,valor):
        combustivelAbastecido = round(valor/self.valorLitro,2)
        if self.verificarQuantidadeDisponivel(combustivelAbastecido):
            self.setQuantidadeCombustivel(self.getQuantidadeCombustivel()-combustivelAbastecido)
            print(f"Vai abastecer {combustivelAbastecido} litros")
            return combustivelAbastecido
        else:
            print("Nao há combustivel suficiente")

    def abastecerPorLitro(self,litro):
        if self.verificarQuantidadeDisponivel(litro):
            valorAPagar = litro * self.valorLitro
            self.setQuantidadeCombustivel(self.getQuantidadeCombustivel()-litro)
            print(f"Vai pagar {valorAPagar} reais")
            return valorAPagar
        else:
            print("Nao há combustivel suficiente")


bomba1 = BombaCombustivel("Gasolina", 7.5, 10000)
bomba2 = BombaCombustivel("Disel", 5.88,0)
bomba1.abastecerPorLitro(102)
print(bomba1.getQuantidadeCombustivel())
bomba2.abastecerPorValor(304)
bomba2.setQuantidadeCombustivel(400)
bomba2.abastecerPorValor(304)
print(bomba2.getQuantidadeCombustivel())



