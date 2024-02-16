try:
    nombre=input("Cual es tu nombre?")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es: " + nombre
    print(nombre_usuario)    
except:    
    print("Ha ocurrido un error")

#Multiple excepciones

try:
    numero = int(input("Numero para elevarlo al cuadrado"))
    print(f"El cuadrado es: {numero*numero}")        
except TypeError:
    print("Debes convertir tis cadenas a enteros en el codigo")
except ValueError:
    print("Introduce un numero correcto")        
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error: ", type(e).__name__)    

#Excepciones personalizadas
try:
    name = input("Introduce tu nombre: ")         
    age = int(input("Introduce la edad: "))

    if age < 5 or age >110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <=1:
        raise ValueError("Introduce bien tu nombre")
    else:
        print(f"Bienvenido {name}")
except ValueError:
    print("Introduce lo datos correctamente")
except Exception as e:
    print("Existe un error: ", e )    