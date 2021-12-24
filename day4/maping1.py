
def cordenadas(map):
    fila = None #primer numero
    colum = None # segundo numero  queda en 3 
    for fila in range(0, len(map)):# fila = 1 map[1]
        for colum in range(0, len(map[fila])): # colum = 0 map[1][0]
            if map[fila][colum] == "X":
                print(map[fila][colum])
                print(fila, colum)
                return fila, colum
            print(fila, colum)

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","X","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(map)

print(cordenadas(map))
            