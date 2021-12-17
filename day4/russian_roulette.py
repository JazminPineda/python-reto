import random
persons = input("Escriba los participantes separados por una coma ")
separado = persons.split(", ")
print(separado)

random_integer = random.randint(0, len(separado)-1)
print(random_integer)
for i, namen in enumerate(separado):
    if i == random_integer:
        persons[int(i)]
        print(f"{namen} is going to buy the meal today!")

# Mas sencillo y no supe porque 

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
random_integer = random.randint(0, len(names)-1) #se le incluye unicamente el -1
print(f"{names[random_integer]} is going to buy the meal today!")
#352354234
#Tom, Dick, Harry dick  tom

#345234
#Angela, Jane, Jeremy, Tom, Robin robin
