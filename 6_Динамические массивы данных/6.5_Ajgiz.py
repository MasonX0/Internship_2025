import numpy as np
Final=[]
ListOfBuildings = []
ListOfFloors = []
List=[]
choice = int(input("1 - ввод с клавиатуры, 2 - с файла : "))
if choice == 1:
    line = input("Введите как в примере 1_5_23 ч\з пробел:")
    incomplitedlist = line.split(" ")
if choice == 2:
    with open("DataOfRooms.txt", 'r', encoding='utf-8') as file:
        line = file.readline()
    incomplitedlist = list(line.split(" "))

for i in incomplitedlist:
    List.append(i.split("_"))
    ListOfFloors.append(i.split("_")[-2])
    if (i.split("_")[0]) not in ListOfBuildings: ListOfBuildings.append(i.split("_")[0])
for i in ListOfBuildings:
    maxinBuilding = 0
    for g in ListOfFloors:
        infloor = 0
        for j in List[1:]:
            if i == j[0] and g == j[-2]:
                infloor += int(j[-1])
        if infloor > maxinBuilding:
            maxinBuilding = infloor
    Final.append([int(i), maxinBuilding])
maxc = Final[0][-1]
numberofmax = Final[0][0]
for i in Final[1:]:
    if i[-1] > maxc:
        maxc = i[-1]
        numberofmax = i[0]
        print(i)
print("Самый заселенный этаж находится в  {}  общежитии, там живет  {}  человек.".format(numberofmax, maxc))
