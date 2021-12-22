row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizonal = int(position[0]) #primer numero
vertical = int(position[1]) # segundo numero  queda en 3 

# se debe restar uno para que no este fuera del rango FILA
# y se guardar en una variable

# select_row = map[vertical -1]
# select_row[horizonal-1] ="X"


# cuando no se la coordenada
for f in range(0, len(map)):
    if f == vertical - 1:
        for c in range(0, len(map[f])):
            if c == horizonal - 1:
               map[f][c] ='X' 



print(f"{row1}\n{row2}\n{row3}")
        

    
    
    
        



   
