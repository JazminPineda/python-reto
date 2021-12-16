import random

#primera forma
# ramdom_int = random.randint(1,5) # ramdom decimales del 0 al 10
# random_float = random.random() # ramdom decimales del 0 al 1
# print(random_float*ramdom_int)

#segunda forma print(random.uniform(0.0,5)) # ramdom decimales del 0 al 5

print("Wellcom random coin! Heand or Tails?")
resultado= random.randint(0,1)

if resultado == 1:
    print("Heads")
else:
    print("Tails") 

