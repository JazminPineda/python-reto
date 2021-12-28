
# sumar del 1 al 100
suma= 0
for numer in range(1, 101):
    suma = numer + suma
print(suma)

# sumar numeros pares del 1 al 100

suma= 0
for numer in range(2, 101, 2):
    suma = numer + suma
print(suma)

suma_2=0
for numer in range(1, 101):
    if numer % 2 == 0:
        suma_2 += numer
print(suma_2)