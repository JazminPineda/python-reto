import random

#primera forma
# ramdom_int = random.randint(1,5) # ramdom decimales del 0 al 10
# random_float = random.random() # ramdom decimales del 0 al 1
# print(random_float*ramdom_int)

#segunda forma print(random.uniform(0.0,5)) # ramdom decimales del 0 al 5

# print("Wellcom random coin! Heand or Tails?")
# resultado= random.randint(0,1)

# if resultado == 1:
#     print("Heads")
# else:
#     print("Tails") 

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])

print(dirty_dozen)
#Then print out:

print(dirty_dozen[0])
print(dirty_dozen[1])
#To see what happens at the next stage print out:

print(dirty_dozen[1][2])
print(dirty_dozen[1][3])