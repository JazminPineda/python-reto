#Prueba de listas de frutas y ejecuciòn con un for
# fruits=["Piniapple","Peach", "Pear", "Apple"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " "+" Pie")
#lista1= [180, 124, 165, 173, 189, 169, 146]
# lista2=[]
# student_heights=0
# total=0
# contar=0

# salir = "no"
# while salir == "no":
#     student_heights = int(input("Input a list of student heights "))
#     lista2.append(student_heights)
#     contar +=1 
#     total = student_heights + total
#     salir= input("Desea salir? (si o no)")

# promed = round(total/ contar)
# print(lista2, contar, total, promed)
student_heights = input("Input a list of student heights ").split()
print(type (student_heights), student_heights)
for n in range(0, len(student_heights)):
   student_heights[n] = int(student_heights[n])

contador = 0
sumar=0
for height in range(0, len(student_heights)):
   sumar = student_heights[height] + sumar
   contador +=1
promedio= round(sumar/contador)
 
print(sumar, contador, promedio)

