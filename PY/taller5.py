#TALLER 5 PYTHON
#AUTOR: DANIEL OSORIO QUIMBAYO
#FECHA: 03/11/2023

from datetime import date
hoy = date.today()
print("Hoy es el día: ", hoy)

print("TALLER 5 CICLOS ITERATIVOS CON LA SENTENCIA FOR")

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
print("Ciclo para el primer numero")
for i in range(num1):
    print(i)
print('Fin del ciclo')    

print("Ciclo desde el primer numero hasta el segundo")
for j in range(num1,num2):
    print(j)
print('Fin del ciclo')

print("Ciclo desde el primer numero hasta el segundo con incrementos de 3")
for k in range(num1,num2,3):
    print(k)
print('Fin del ciclo')

empresa = input("digite nombre de una empresa: ")
empresa = empresa.lower()
for character in empresa:
    print(character)
print('Fin del ciclo')    

print('FIN')