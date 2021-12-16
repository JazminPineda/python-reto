print('''
                                                     88                       
                                                     88                       
                                                     88                       
 ,adPPYb,d8 ,adPPYYba, 88,dPYba,,adPYba,   ,adPPYba, 88,dPPYba,   ,adPPYba,   
a8"    `Y88 ""     `Y8 88P'   "88"    "8a a8P_____88 88P'    "8a a8"     "8a  
8b       88 ,adPPPPP88 88      88      88 8PP""""""" 88       d8 8b       d8  
"8a,   ,d88 88,    ,88 88      88      88 "8b,   ,aa 88b,   ,a8" "8a,   ,a8"  
 `"YbbdP"Y8 `"8bbdP"Y8 88      88      88  `"Ybbd8"' 8Y"Ybbd8"'   `"YbbdP"'   
 aa,    ,88                                                                   
  "Y8bbdP"                                                                    
             
             
''')

print("Welcome to Tresure Island \
Your mission is to find the treasure.")
paso = input("You´re at a cross road. Where do you want to go? Type 'left' or 'right'")
if paso == "left":
    paso1= input("You come to a lake. There is an islan in the middle of the lake. Type 'wait' to wait for a boat. \
                Type 'swim' to swim across")
    if paso1 == "wait":
        puerta = input("which door would you like to go through? red, yellow, or blue.")
        if puerta == "red":
            print("game over xc")
        elif puerta == "yellow":
            print("you'll end up with")
        else:
            print("winning the game")


    if paso1 == "swim":
        paso1_1 = input("nada rapido estan que te atrapan, que haces te 'undes'  \
            y dejas que te 'atrapen'?")
        if paso1_1 =='undes':
            lio = input("uff estuvo cerca, pero viene una vibora, tienes dos opciones 'matarla'\
                 o dejarla 'viva'")
            if lio == "matarla":
                print("winning the game")
            else:
                print("game over xc")
else:
    print("game over")       
##ascii.co.uk/art