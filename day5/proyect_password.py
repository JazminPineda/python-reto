import string
import random


def list_alfabeth():
    return  string.ascii_lowercase + string.ascii_uppercase

def get_code():
    return string.punctuation

print("Welcome to the Pypassword Generator!")
letters=int(input("How many letters would you like in your password? "))
simbols=int(input("How many symbols would you like? "))
numers=int(input("How many numbers would you like? "))
list_alfabeth()
abecedario= list_alfabeth()
simbolos = get_code()

numeros=[]
for numero in range(0, 10):
    numeros.append(str(numero))
numeros

password =  random.sample(abecedario, k=letters)+random.sample(numeros, k=numers)+random.sample(simbolos, k=simbols)
#print('original', password)
random.shuffle(password)
#print('mezclado lista', password)
#'lo mezclado string' 
password="".join(password)
print(f"Here is your password: {password}")
