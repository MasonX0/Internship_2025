# Part 2 Number of students in a group
import numpy as np

choice = int(input("1 - ввод с клавиатуры, 2 - с файла -  : "))
if choice == 1:
    recruitedList = input("Вводите рост учеников через пробел: ")
    listOfStudents = list(map(float, recruitedList.split()))
elif choice == 2:
    listOfStudents = np.loadtxt("ListOfStudents_Ajgiz.txt")
else:
    listOfStudents = np.loadtxt("ListOfStudents_Ajgiz.txt")
cnt=0
for i in listOfStudents:
    if i>(sum(listOfStudents)/(len(listOfStudents)-1)): #Ноль не стал учитывать
        cnt+=1

print("Количество учащихся группы, чей рост выше среднего", cnt)
print(sum(listOfStudents)/(len(listOfStudents)-1))
