import random
#generar le aleatorio = simular el lanzamiento de una moneda 
lanzamiento = random.randint(0,1)



# usuario selecione cara o sello
# eleccion es la entrada del ejercicio 

eleccion = int(input("ingrese 0 para cara o 1 para sello: "))
print(f"el lanzamiento fue: {lanzamiento}")


# determinar si el usuario gano o perdio
#procesos del ejercicio

if eleccion == lanzamiento:
    print("¡Ganaste!")
else:
    print("Perdiste.")
    
# que el 0 sea cara y el 1 sea sello
if lanzamiento == 0:
    print("La moneda cayó en cara.")        
else:    print("La moneda cayó en sello.")
    # error al colocar un numero diferente a 0 o 1
if eleccion != 0 and eleccion != 1:
    print("Error: Debes ingresar 0 para cara o 1 para sello.")  
    
