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
    
    