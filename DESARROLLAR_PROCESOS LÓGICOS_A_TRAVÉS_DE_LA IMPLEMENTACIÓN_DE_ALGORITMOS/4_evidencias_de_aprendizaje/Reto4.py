"""Desarrolle un programa en Python que le permita generar la

simulación del juego piedra, papel o tijera (juego contra la máquina)

❑ Determine y muestre en pantalla el resultado del juego, si gana

alguien o hay empate."""
import random
# Generar la elección de la máquina (0 para piedra, 1 para papel, 2 para tijera)
opciones=("piedra","papel","tijera")
maquina = random.randint(0, 2)
# Solicitar al usuario que ingrese su elección          
usuario = input("Elige piedra, papel o tijera: ")
# Validar la elección del usuario
if usuario not in opciones:
    print("Elección inválida. Por favor, elige piedra, papel o tijera.")
else:
    # Mostrar las elecciones
    print(f"Tu elección: {usuario}")
    print(f"Elección de la máquina: {opciones[maquina]}")
    
    # Determinar el resultado
    if usuario == opciones[maquina]:
        print("¡Es un empate!")
    elif (usuario == "piedra" and opciones[maquina] == "tijera") or \
         (usuario == "papel" and opciones[maquina] == "piedra") or \
         (usuario == "tijera" and opciones[maquina] == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!") 
        
