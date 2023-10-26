#TALLER 4 PYTHON
#AUTOR: DANIEL OSORIO QUIMBAYO
#FECHA: 26/10/2023

from datetime import date
hoy = date.today()
print("Hoy es el día: ", hoy)

print("EJERCICIO DE LAS CLASES DE TRIANGULOS")
a = int(input("digite el valor de A: "))
b = int(input("digite el valor de B: "))
c = int(input("digite el valor de C: "))

if(a==b and a==c and b==c):
    print("EL TRIANGULO ES EQUILATERO")
else:
    if (a==b or b==c or a==c):
        print("EL TRIANGULO ES ISOCELES")
    else:
        print("EL TRIANGULO ES ESCALENO")        

animal = input("digite un animal: ")
animal = animal.upper()
if animal == "PERRO":
    print (f"Este animal es el mejor amigo del hombre: {animal}")
elif animal == "GATO":
    print(f"Este animal persigue a los ratones: {animal}")    
elif animal == "OSO":
    print(f"Este animal vive en el polonorte: {animal}")
else:
    print(f"No es PERRO, no es GATO, tampoco un OSO es un {animal}")    

print("FIN")