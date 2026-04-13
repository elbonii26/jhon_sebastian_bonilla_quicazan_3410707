"""Craps apuestas a un solo tiro, en este juego se lanzan dos dados, se
gana si se obtiene un lanzamiento con

❑ Un par de unos en los dados.
❑ Un total de tres en los dados.
❑ Un total de once en los dados.
❑ Si se obtiene dos o doce en los dados.
❑ Un total de siete en los dados.
En el resto de situaciones se pierde.
Realiza un programa en Python que te permita jugar craps"""

import random     
# Simular el lanzamiento de dos dados
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
# Calcular el total de los dados
total = dado1 + dado2
print(f"Has lanzado los dados: {dado1} y {dado2}. Total: {total}")
# Determinar si el jugador gana o pierde
if (dado1 == 1 and dado2 == 1) or total == 3 or total == 11 or total == 2 or total == 12 or total == 7:
    print("¡Ganaste!")
else:
    print("¡Perdiste!")


