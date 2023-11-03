#TALLER 3 PYTHON
#AUTOR: DANIEL OSORIO QUIMBAYO
#FECHA: 03/11/2023

from datetime import date
hoy = date.today()
print("Hoy es el día: ", hoy)

a = int(input("Digite el valor de A: "))
b = int(input("Digite el valor de B: "))
if a >= b:
    print("A es mayor o igual a B")
else:
    print("B es mayor que A ")

curso1 = "Requerimientos"
curso2 = "Algoritmos"
print(f"El curso1 es: {curso1}")
print(f"El curso2 es: {curso2}")
if curso1 == "Requerimientos" and curso2 == "Algoritmos":
    print("Usted estudia Programacion de software")
else:
    print("Usted estudia otro programa")    

print("*** Final del Analisis Del programa ***")

frase = input("Digite una oracion: ")
print(f"La frase en mayuscula es: {frase.upper()}")
longitud = len(frase)
print(f"La longitud de la frase es: {longitud} caracteres")
if longitud > 10:
    print("La frase tiene más de 10 caracteres")
else:
    print("La frase tiene menos de 11 caracteres")
print("FIN")     