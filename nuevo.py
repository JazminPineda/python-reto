# print('Welcome to the Band Name Generator')
# city= input("What`s name of the city you grew up in?\n")
# pea= input('What`s your pet`s name? \n')
# print(f"Your band name could be {city} {pea}")



# #calculadora
# print('Welcome to the tip calculator')
# total = float(input('What was the total bill $ '))
# people = float(input('How many people to split the bill? '))
# percen= float(input("What percentage tip would you like to give? 10, 12, or 15? "))
# n1= total
# n2= percen
# n3= people
# subt= (n2/100)*n1
# n4= n1+subt
# divido = n4 /n3
# print(f"Each person should pay:${divido:0.1f}", )


# weight = int(input("enter your weight in kg: "))
# height = float(input("enter your height in m:"))
# bmi = int(weight/(height**2))
# print(bmi)

# print(height**2)

#two_digit_numer= input("Type a two digit numer: ")
# #print(int(two_digit_numer[0])+int(two_digit_numer[1]))
# acumulado = 0
# for n in range(0, len(two_digit_numer)): 
#     acumulado= acumulado + int(two_digit_numer[n])
#print(acumulado)
#@PEMDASLR
    
#Tiene error ya que no es un str y no se puede concatenar
# name=12
# print("hello,"+name+"real")

# number = int(input("Which number do you want to check? "))
# #Write your code below this line 👇
# par= number%2
# if par == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

#estoy en el 29

# age = int(input("What is your current age? "))

# falta = 90 - age
# d = (365 * falta)
# w = (52 * falta)
# m = (12 * falta)


# print(f"You have {d} days, {w} weeks, and {m} months left.")

# calculadora corporal 
# height = float(input("enter your height in m: "))
# weight = int(input("enter your weight in kg: "))

# bmi= weight/(height**2)

# if bmi <=18.5:
#     print(f"Your BMI is {bmi:1.0f}, you are underweight.")
# elif bmi >18.5 and bmi <= 25:
#     print(f"Your BMI is {bmi:1.0f}, you have a normal weight.")
# elif bmi >25 and bmi <= 30:
#     print(f"Your BMI is {bmi:1.0f}, you are slightly overweight.")
# elif bmi >30 and bmi <= 35:
#     print(f"Your BMI is {bmi:1.0f}, you are obese.")
# else:
#     print(f"Your BMI is {bmi:1.0f}, you are clinically obese.") 


#year = int(input("Which year do you want to check? "))

#Mas estructurado
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.") 
#         else:
#             print("Leap year." ) 
#     else:
#         print("Leap year." ) 
# else:
#     print("Leap year." ) 
#Primer intento
# r1= year%4
# r2= year%100
# r3= year%400

# if r1 == 0:
#     if r2>= 0 or r3==0:
#         print("Leap year." ) 
#     else:
#         print("Not leap year.")   
# else:
#     print("Not leap year.") 

# S = 15
# M = 20
# L = 25
# bill = 0
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# if size == "S":
#     bill = bill + S
#     if add_pepperoni == "Y":
#         bill += 2  
# elif size == "M":
#     bill += M
#     if add_pepperoni == "Y":
#         bill += 3 
# else:
#     bill += L
#     if add_pepperoni == "Y":
#             bill += 3
# if extra_cheese =="Y":
#     bill += 1
# print(f"Your final bill is: ${bill}.")

#Montaña RUSA

# height=int(input("What is your height in cm? "))
# bill = 0
# print("You can ride the rollercoaster")
# if height >= 120:
#     age=int(input("What is your age "))
#     foto=input("Do you want a photo token? Y or N ")
#     if  age <= 12:
#         bill += 5
#     elif age >12 and age <=18:
#         bill += 7
#     elif age >= 19:
#         if age >=45 and age <=55:
#             bill += 0
#             print("Everything's going to be ok. Have a free ride on us!")
#         else:
#             bill += 12
        
    
#     if foto == "Y":
#         bill += 3
#     print(f"Your final bill is ${bill}")
# else:
#     print("Sorry, you have to grow taller before you can ride.") 

## PROGRAMA CALCULADORA DEL AMOR Love Calculator!
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
names= (name1+name2).upper()
resultado = 0
resultado2 = 0
puntaje1 ="TRUE"
puntaje2 ="LOVE"

for pos, char  in enumerate(puntaje1):
    for pos1, char1 in enumerate(names):
        if char1 == char:
            resultado += 1
for pos, char  in enumerate(puntaje2):
    for pos1, char1 in enumerate(names):
        if char1 == char:
            resultado2 += 1   
final= str(resultado) + str(resultado2)
fin= int(final)
if fin <= 10 or fin >=90:
    print( f"Your score is {fin}, you go together like coke and mentos.")
elif fin >= 40 and fin <= 50:
    print(f"Your score is {fin}, you are alright together.")
else:
    print(f"Your score is {fin}.")
  

    
        
    

  


