import numpy as np
s1 = 0
s2 = 0
s3 = []
cnt = 0
sr = 0
endlist=[]
choice = int(input("1 - ввод с клавиатуры, 2 - автозаполнение, 3 - с файла : "))
if choice == 1:
    recruitedList = input("Введите числа :")[:-2]
    slist = list(recruitedList.split("-1"))
    for i in slist:
        smlist = list(i)
        endlist.append(smlist)
        s1 += sum(int(x) for x in list(i))
        s2 += len(list(i))
        s3.append(max(list(i)))
    srvse = s1 / s2
    for i in s3:
        if float(i) > srvse:
            cnt += 1
if choice==2:
    cnt1=int(input("Введите количество учеников: "))
    for i in range(cnt1):
        numberofstudentsgrades=int(np.random.randint(low=7,high=14))
        gradeslist = np.random.randint(low=2,high=6,size=numberofstudentsgrades)
        s1 += sum(int(x) for x in gradeslist.tolist())
        s2 += len(gradeslist.tolist())
        endlist.append(gradeslist.tolist())
        s3.append(max(gradeslist.tolist()))
    srvse = s1 / s2
    for i in s3:
        if float(i) > srvse:
            cnt+=1
if choice==3:
    with open("DataOfGrades.txt", 'r', encoding='utf-8') as file:
        listOfTemperatures = file.readline()[:-2]
    slist = list(listOfTemperatures.split("-1"))

    for i in slist:
        smlist = list(i)
        endlist.append(smlist)
        s1 += sum(int(x) for x in list(i))
        s2 += len(list(i))
        s3.append(max(list(i)))
    srvse = s1 / s2
    for i in s3:
        if float(i) > srvse:
            cnt += 1
print("Список оценнок группы: \n",endlist)
print("Средний балл по группе: ",srvse)
print("Количество учащихся группы, чей максимальный балл за семестр ниже среднего: ",cnt)
