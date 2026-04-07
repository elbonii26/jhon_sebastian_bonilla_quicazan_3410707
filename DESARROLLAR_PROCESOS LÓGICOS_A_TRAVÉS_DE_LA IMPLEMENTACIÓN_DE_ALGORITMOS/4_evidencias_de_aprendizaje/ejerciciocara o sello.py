import random
# elige un opcion entre cara o sello
opcion = input("elige cara o sello: ")
maquina = random.choice(["cara", "sello"])
print(f"la maquina eligio {maquina}")
# COMPARA SI GANO O PERDIO 
if opcion == maquina:
    print("ganaste")
else:
    print("perdiste")       
    







                

