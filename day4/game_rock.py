import random

def print_jugada(jugador):
    rock= '''

            ,--.--._
    ------" _, \___)
            / _/____)
            \//(____)
    ------\     (__)
        `-----"
    
        '''
    paper= '''
                ___..__
    __..--""" ._ __.'
                "-..__
                '"--..__";
    ___        '--...__"";
        `-..__ '"---..._;"
            """"----'   
        '''

    sissors= '''
        
        .-.  _
        | | / )
        | |/ /
    _|__ /_
    / __)-' )
    \  `(.-')
    > ._>-'
    / \/

        '''
    games={"0":rock, "1":paper, "2":sissors}
    for clave in games:
        if clave == jugador:
            print(games[clave])
   
       

print("Wellcom games rock, paper and scissonrs")
game_one= str(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissonrs "))  
while int(game_one) < 0 or int(game_one) >=3:
    print("You type an invalid number, you lose!")
    game_one= str(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissonrs "))  

print_jugada(game_one)
game_two= str(random.randint(0,2))
print(f"Jugada PC elige: {game_two}")
print_jugada(game_two)

    
if game_one == "0" and game_two=="2":
    print("You win")
elif game_two =="0" and game_one=="2":
    print("You lose")
elif game_two > game_one: # fijese que se pone de primera la computadora porque el puntaje cumple si es mayor q
    print("You lose")
elif game_one > game_two:
    print("You win")
elif game_one == game_two:
    print("It`s a draw")
else:
    print("You type an invalid number, you lose!")

#Una manera de hacerlo
# if game_one == "0" and game_two=="2":
#     print("You win")
# elif game_one == "2" and game_two=="1":
#     print("You win")
# elif game_one == "1" and game_two=="0":
#     print("You win")
# elif game_one == game_two:
#     print("it`s a draw")
# else:
#     print("You lost, computer win!")








    
    