import random

print("Wellcom games rock, paper and scissonrs")
game_one= int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissonrs "))

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


games=[rock, paper, sissors]

for i in range(0, len(games)):
    if i == game_one:
        print(games[i])
game_two= random.randint(0,2)
print(game_two)
for i in range(0, len(games)):
    if i == game_two:
        print("Computer chose:")
        print(games[i])



lose= "you lose"
draw= "you had a draw"  
win = "you win"
puntaje = [lose, draw, win ]
for k in range(0, len(puntaje)):
    print(puntaje[k])
    
    