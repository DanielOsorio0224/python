def muestraNombre():
    print("Daniel")

muestraNombre()    

print("#####")
nombre = input("Introduce tu nombre completo: ")
def muestraNombreCompleto(nombre):
    
    print(f"Tu nombre es: {nombre}")

muestraNombreCompleto(nombre)

def tabla(numero):
    contador = 1
    print(f"Tabla del {numero}")
    for contador in range(1,11):
        print(f"{numero}*{contador} = {numero*contador} ")
numero = int(input("Introduce un numero: "))
tabla(numero)        

#Funcion Lambda, funcion de una linea 

year = lambda year: f"El año es {year}"

print(year(2024))