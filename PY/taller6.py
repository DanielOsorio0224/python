#TALLER 6 PYTHON
#AUTOR: DANIEL OSORIO QUIMBAYO
#FECHA: 03/11/2023

from datetime import date
hoy = date.today()
print("Hoy es el día: ", hoy)
print("TALLER 6 CICLOS ITERATIVOS CON LA SENTENCIA WHILE")

num1 = int(input("Ingrese un numero: "))
print("***Ciclo controlado por contador")
i = 1
while i <= num1:
    print(i)
    i += 1
print('Fin del ciclo')    

print('***Ciclo controlado por evento')

i = 1
numero1 = 5
numero2 = int(input('Ingrese un numero del 1 al 10: '))
while numero2 != numero1:
    i += 1
    numero2 = int(input('Digite otro numero del 1 al 10: '))
print(f'Acertaste en el intento n°{i}')
print('Fin del ciclo')    

print('***Ciclo abortado con la sentencia BREAK')
amistad = input('Ingrese nombre de una persona: ')
amistad = amistad.upper()
for caracter in amistad:
    print(caracter)
    if caracter =="A":
        print('HASTA AQUI LLEGASTE')
        break
print('Fin del ciclo')    
print('FIN')