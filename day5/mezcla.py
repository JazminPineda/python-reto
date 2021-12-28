import random

lista = ['rojo', 'verde', 'amarillo']

random.shuffle(lista)
print('mezcla1', lista)

random.shuffle(lista)
print('mezcla2', lista)
print(lista[random.randint(0,2)])