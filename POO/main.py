class Coche:
    color = "Rojo"
    marca = "Chevrolet"
    modelo = "Sail LS"
    velocidad = 160
    fuerza = 1399
    capacidad = 5

    def setColor(self,color):
        self.color = color

    def getColor(self):
        return self.color    

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -=1

    def getVelocidad(self):
        return self.velocidad        
    
coche = Coche()

coche.acelerar()
print(coche.getVelocidad())
coche.setColor("Azul")
print(coche.getColor())

coche2 = Coche()
print(coche2.getColor())