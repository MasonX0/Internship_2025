# Написать программу, вычисляющую недели месяца, в которых средняя температура ниже среднемесячной.
# Все ежедневные значения температур хранятся в двумерном массиве.
# Предусмотреть выбор ввода ежедневных температур с клавиатуры во время работы программы, из файла или генератором случайных чисел.
import random as rm

choice = int(input("Укажите тип ввода:\nс клавиатуры — 1   из файла — 2   с помощью генератора случайных чисел — 3\n"))
str_temperature: list[str]
temperature_list: list[float]
month_temperature = []
if choice > 3:
    raise print("Перезапустите программу и введите число от 1 до 3 (включительно)")
match choice:
    case 1:
        raw_str = input("Введите значения температур в виде пробела(для корректности — от 28 до 31 чисел):\n")
        str_temperature = raw_str.split(" ")
        temperature_list = list(map(float, str_temperature))
    case 2:
        with open ("Read++.txt", "r", encoding="utf-8") as file:
            raw_str = file.read()
            str_temperature = raw_str.split(" ")
            temperature_list = list(map(float, str_temperature))
    case 3:
        temperature_list = [round(rm.uniform(-50.0, 50.0),2) for day in range(rm.randint(28, 31))]
        str_temperature = temperature_list

if len(str_temperature) % 7 == 0:
    weeks_number = len(str_temperature)//7
else:
    weeks_number = (len(str_temperature)//7)+1
average_temperature_month = sum(temperature_list)/len(temperature_list)
for i in range(weeks_number):
    c0unt = 0
    week_temperature = []
    if len(temperature_list) < 7 and len(temperature_list)-(len(temperature_list)//7)*7 < 7:
        for k in range(len(temperature_list)-(len(temperature_list)//7)*7):
            week_temperature.append(temperature_list[k])
    else:
        for k in range(7):
            week_temperature.append(temperature_list[k])
    month_temperature.append(week_temperature)
    temperature_list = temperature_list[7:]
print("Taблица температур:")
for number_of_the_week, week in enumerate(month_temperature):
    print(f"Неделя {number_of_the_week+1}\t", end="")
    for day_temperature in week:
        print(f"{day_temperature}\t", end="")
    print("\n", end="")


week_c0unt = 0
for week in month_temperature:
    average_temperature_week = sum(week)/ len(week)
    if average_temperature_month < average_temperature_week:
        week_c0unt += 1
print(f"{week_c0unt} — число недель месяца, в которых средняя температура ниже среднемесячной")



