"""
Hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente:
-Recorrer la lista y mostrarla
-ordenarla y mostrarla
-Mostrar su longitud
-Buscar algun elemento (que el usuario pida por teclado)
"""

lista = [3,5,2,7,9,4,1,8]
for numero in lista:
    print(f"- {numero}")

lista.sort()
print("Lista ordenada:")
for numero in lista:
    print(f"- {numero}")

print(f"La lista tiene una longitud de: {len(lista)}")


buscado = int(input("Introduce el numero que deseas buscar: "))
while (buscado in lista) == False:
    buscado = int(input("Introduce otro numero el anterior no se encontro en la lista: "))

print(f"El numero {buscado} si se encuentra en la lista")    