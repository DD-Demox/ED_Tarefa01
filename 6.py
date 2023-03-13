class TV:
    def __init__(self, canal=1, volume=5):
        self.canal = canal
        self.volume = volume

    def mudarCanal(self, canal):
        if 0 < canal < 99:
            self.canal = canal
            return self.canal
        else:
            return "Canal Invalido"

    def aumentarVolume(self):
        if self.volume < 10:
            self.volume = self.volume + 1
        return self.volume
    def diminuirVolume(self):
        if self.volume > 0:
            self.volume = self.volume - 1
        return self.volume


tvArmando = TV()
print(tvArmando.mudarCanal(100))
print(tvArmando.mudarCanal(23))

for i in range(7):
    print(tvArmando.aumentarVolume())

for i in range(14):
    print(tvArmando.diminuirVolume())