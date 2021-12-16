import random

print("Wellcom games rock, paper and scissonrs")
pc= random.randint(0,2)

for i in range(0,2):
    game_one= int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissonrs "))
game_two= pc

if game_one == 0:
    print('''

        ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
 
    ''')
if game_one == 1:
    print('''
               ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'   
    ''')

if game_one == 2:
    print('''
    
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/

    ''')