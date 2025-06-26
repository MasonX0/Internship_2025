import numpy as np
# Part 3 weeks of the month in which the average temperature is below the monthly average.
choice = int(input("1 - ввод с клавиатуры, 2 - автозаполнение, 3 - с файла : "))
if choice == 1:
    first = []
    second = []
    recruitedList = input("Введите числа через пробел, образец -> 30gradПн :")
    list = list(recruitedList.split())
    for i in list:
        part1, part2 = i.split("grad")
        first.append(int(part1))
        second.append(part2)
elif choice == 2:
    month = None
    for i in range(4):
        days = np.array(['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'])
        first = np.random.uniform(low=15, high=35, size=7)
        matrix = np.column_stack((first, days))

        if month is None:
            month = matrix
        else:
            month = np.vstack((month, matrix))
elif choice == 3:
    month = None
    with open("Data&Temperature.txt", 'r', encoding='utf-8') as file:
        listOfTemperatures = file.readline()
    list = list(listOfTemperatures.split())
    for i in list:
        first = []
        second = []
        part1, part2 = i.split("grad")
        first.append(float(part1))
        second.append(part2)
        matrix = np.column_stack((first, second))
        if month is None:
            month = matrix
        else:
            month = np.vstack((month, matrix))
summ = 0
for i in month:
    summ += float(i[0])
AverageOnMonth = summ / len(month)
print("Среднемесячная температура: ", AverageOnMonth)
listOfTemperaturesForWeeks = []
while len(month) >= 7:
    correctedmonth = month[:7]
    month = month[7:]
    s = 0
    for i in correctedmonth:
        s += float(i[0])
    listOfTemperaturesForWeeks.append(s / 7)
if 0 < len(month) < 7:
    s = 0
    for i in month:
        s += float(i[0])
    listOfTemperaturesForWeeks.append(s / len(month))
cnt = 0
for i in listOfTemperaturesForWeeks:
    if i < AverageOnMonth:
        cnt += 1
print("Средние температур недель: ", listOfTemperaturesForWeeks)
print("Количество недель, в которых средняя температура ниже среднемесячной", cnt)
