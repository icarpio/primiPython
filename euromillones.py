from random import sample

print("\nLa combinacion de la suerte hoy es: \n")
numeros=sorted(sample(range(1,51),5))
stars = sorted(sample(range(1,12),2))

print(f'Numeros: {numeros} y estrellas: {stars}')





