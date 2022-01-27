import math

def calculat_area(alto, ancho, cober):
     area = alto * ancho
     cubetas = area /5
     cubetas = round(cubetas, 1)
     num_cub = math.ceil(area / cober)

     print(f"Debes comprar {cubetas:0.0f} cubetas, nex result {num_cub}")


alto = int(input("cuanto de alto tiene m2? "))
ancho= int(input("cuanto de ancho tiene m2? ")) 

calculat_area(alto, ancho, cober = 5)

