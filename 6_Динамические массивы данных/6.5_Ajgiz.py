import numpy as np
fs=[]
Ls = []
Itog = []
Ls1 = []
LsRooms = []
LsBuild = []
LsFlours = []
choice = int(input("1 - ввод с клавиатуры, 2 - автозаполнение, 3 - с файла : "))
if choice == 1:
    List = input("Введите как в примере 1_5_23 ч\з пробел:")
    List1 = List.split(" ")
    for i in List1:
        Ls.append(i.split("_"))
        Ls1.append(i.split("_")[:-1])
        LsRooms.append(i.split("_")[-1])
        LsFlours.append(i.split("_")[-2])
        if (i.split("_")[0]) not in LsBuild: LsBuild.append(i.split("_")[0])


for i in LsBuild:
    sffl = 0
    for g in LsFlours:
        sfl = 0
        for j in Ls[1:]:
            if i == j[0] and g == j[-2]:
                sfl+=int(j[-1]) #Нашел сумму комнат на этаже конкр общаги
        if sfl>sffl:
            sffl=sfl
    Itog.append([int(i),sffl])#Добавляю в список этаж с наиб зас-ем в этой общаге
maxc = Itog[0][-1]
numberofmax = Itog[0][0]
for i in Itog[1:]:
    if i[-1] > maxc:
        maxc = i[-1]
        numberofmax = i[0]
        print(i)
print("Саммый заселенный этаж находится в  {}  общежитии, там живет  {}  человек.".format(numberofmax,maxc))

