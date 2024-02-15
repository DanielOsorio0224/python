peliculas = ["Batman","Superman","Avengers"]
colores =list(("Negro","Blanco","Rojo"))

print(colores)

#indices
colores.append("Azul")

print(peliculas[1])
print(peliculas[-1])
print(colores[1:3])

for color in colores:
    print(f"{colores.index(color)}. {color}") 