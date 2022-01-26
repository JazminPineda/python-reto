import os # Ayuda para borrar tan pronto ejecuta algo el usuario
from hangman_art import hangman, logo
from hangman_words import word_list
import string
import random

print(logo, "\n Psst, the solution is thriftless.\n")

for i in range(0, len(hangman)):
    vidas = i

#word_list = ["aardvark", "baboon", "camel"]

word = random.choice(word_list)
print(word)
lista_salida=[]

for i  in range(0,len(word)):
    lista_salida.append("_")
    
print(lista_salida)
end_of_game= False
vidas = len(hangman)
print(vidas)

while vidas > 0: # not end_of_game and 
    letter = input("Guess a letter:").lower() #para no dif minus y may 
    os.system("cls")# Ayuda para borrar tan pronto ejecuta algo el usuario
    lista_entrada=[]
    if letter in word and not letter in lista_salida:
        #True
               
        for ind in range(0, len(word)):
                      
            if word[ind] == letter: #accedo a la palabra por medio del indice
                lista_salida[ind] = letter #teniendo el indice lo reemplazo por la letra del usuario
                                
        print(lista_salida)
    
    elif letter in lista_salida: #Cuando la letra esta repetida pero no quiero quitar life
        print( f"You´ve already guessed {letter}")
    else:
        #False
        
        vidas -= 1
        print(f"You guessed {letter}, that´s not in the word. You lose a life")
        print(hangman[vidas])
        if vidas == 0:
            end_of_game=True
            print("You has lost")
        

    if "_" not in lista_salida:
        end_of_game=True
        print("You has wone")   
