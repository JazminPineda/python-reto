student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

maximo = 0
minimo = 0
for score in range(0, len(student_scores)):
    if student_scores[score] >= maximo:
        maximo = student_scores[score]
    else:
        minimo = student_scores
print(f"The highest score in the class is: {maximo}")
