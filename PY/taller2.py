#TALLER 2 PYTHON
#AUTOR: DANIEL OSORIO QUIMBAYO
#FECHA: 24/10/2023

from datetime import date
hoy = date.today()
print("Hoy es el día: ", hoy)

a = int(input("Digite el primer numero: "))
b = int(input("Digite el segundo numero: "))
c = int(input("Digite el tercer numero: "))
x = [a,b,c]
print("El valor maximo de los numeros ingresados es: ",max(x))
print("El valor minimo de los numeros ingresados es: ",min(x))
print("La suma de los numeros ingresados es: ",sum(x))
z = float(input("digite un numero con decimales: "))
redondo = round(z)
print ("El valor de ", z, "redondeado es: ", redondo)
frase = input("digite una oracion: ")
print("La frase ingresada en mayusculas es: ",frase.upper())
print("La frase ingresada en minusculas es: ",frase.lower())
print("La frase ingresada con la primera letra en mayuscula es: ",frase.capitalize())
print("La frase ingresada con las iniciales en mayusculas de cada palabra es: ",frase.title())
print("La frase ingresada tiene una longitud de: ",len(frase), " caracteres")
print("FIN")