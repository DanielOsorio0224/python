pais = "Colombia"
continente = "america"

print(f"{pais} - {continente}")

# numeros pares del 1 al 100

contador = 1
for contador in range(1,101):
    if contador % 2 == 0:
        print(contador)
        
#Escribir un programa que muestre los cuadrados de los 60 primeros numeros naturales
cont = 1
while cont <= 60:
    print(f"Cuadrado del {cont} = {cont*cont}")
    cont+=1   

cont = 1
for cont in range(1,30):
    print(f"Cuadrado del {cont} = {cont*cont}")    

#Muestra los numeros en el rango dado por el usuario

a = int(input("Escribe el primer numero: "))
b = int(input("Escribe el segundo numero: "))    

for cont in range(a,b):
    print(cont)

# Mostrar todas las tablas de multiplicar

for num1 in range(1,10):
    for num2 in range(1,10):
        print(f"{num1} * {num2} = {num1*num2}")

#El programa tiene que pedir la nota de 15 alumnos y sacar por pantalla cuantos han aprobado

contador = 1
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("Cuantos alumnos tienes"))

while contador <= numero_alumnos:
    nota = int(input(f"Nota del alumno {contador}: ")) 
    if nota >=5 :
        aprobados += 1
    else:
        suspendidos += 1
    
    contador+=1    
print(f"Aprobaron {aprobados} alumnos y reprobaron {suspendidos} alumnos")    