class Coche:
    color = "Rojo"
    marca = "Chevrolet"
    modelo = "Sail LS"
    velocidad = 160
    fuerza = 1399
    capacidad = 5

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -=1

    def getVelocidad(self):
        return self.velocidad        
    
coche = Coche()

coche.acelerar()
print(coche.getVelocidad())