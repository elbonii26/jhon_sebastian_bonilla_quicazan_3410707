"""En Supermercados Noé estamos de aniversario y te obsequiamos un
descuento en el valor de tu compra, si ésta es mayor a 50.000 y
dependiendo de tu suerte:

❑ Si sacas la bolita roja obtienes 10% en el valor de tu compra
❑ Si sacas la bolita azul obtienes un 30% en el valor de tu compra
❑ Si sacas la bolita amarilla obtienes un 50% en el valor de tu compra
❑ Si sacas la bolita blanca te llevas tu compra gratis

Permítale a un cliente del supermercado Noé saber si su compra ha sido
beneficiada con su promoción de aniversario, indique acorde a la bolita
obtenida de forma aleatoria qué valor de descuento ha ganado y cual sería
su valor final a pagar."""
import random
# Solicitar al usuario el valor de su compra                
valor_compra = float(input("Ingrese el valor de su compra: "))
# Verificar si la compra es mayor a 50.000 para aplicar el descuento
if valor_compra > 50000:
    # Generar un número aleatorio entre 0 y 3 para determinar la bolita
    bolita = random.randint(0, 3)
    # Asignar el descuento según la bolita obtenida
    if bolita == 0:
        descuento = 0.10
        print("¡Has sacado la bolita roja! Obtienes un 10% de descuento.")
    elif bolita == 1:
        descuento = 0.30
        print("¡Has sacado la bolita azul! Obtienes un 30% de descuento.")
    elif bolita == 2:
        descuento = 0.50
        print("¡Has sacado la bolita amarilla! Obtienes un 50% de descuento.")
    else:
        descuento = 1.00
        print("¡Has sacado la bolita blanca! Tu compra es gratis.")
    
    # Calcular el valor final a pagar después del descuento
    valor_final = valor_compra * (1 - descuento)
    print(f"El valor final a pagar es: {valor_final:.2f}")
else:
    print("Tu compra no es elegible para el descuento. El valor a pagar es: {:.2f}".format(valor_compra))       

    