# 1. Написать программу, вычисляющую среднюю, максимальную, минимальную за неделю температуру воздуха (3 различные функции).
# Все ежедневные значения температур хранятся в одномерном массиве.
# Предусмотреть выбор ввода ежедневных температур с клавиатуры во время работы программы, из файла или генератором случайных чисел.

import random as rm

def average_temperature(temperature_list: list):
    summ = 0
    for i in temperature_list:
        summ += i
    averageTemperature = summ/ len(temperature_list)
    return averageTemperature

def minimum_temperature(temperature_list: list):
    min_temp = 1000000000000000000000000
    for i in temperature_list:
        if i < min_temp:
            min_temp = i
    return min_temp

def maximum_temperature(temperature_list: list):
    max_temp = 0
    for i in temperature_list:
        if i > max_temp:
            max_temp = i
    return max_temp


choice = input("Выберите тип ввода:\nс клавиатуры — 1   из файла — 2   с помощью генератора случайных чисел — 3\n")
match choice:
    case "1":
        temperature_str = input("Введите 7 значений температур через пробелы\n")
        temperature_list_str= temperature_str.split(sep = " ")
        temperature_l1st = list(map(float , temperature_list_str))
    case "2":
        with open("Read.txt", "r", encoding="utf-8") as file:
            temperature_str = file.read()
            temperature_list_str = temperature_str.split(sep=" ")
            temperature_l1st = list(map(float, temperature_list_str))
    case "3":
        temperature_l1st = [rm.uniform(-100.0, 100.0) for _ in range(7)]

print(f"Значения температуры в течение недели:\n{temperature_l1st}")
print(f"Cредняя температура = {average_temperature(temperature_l1st)}")
print(f"Максимальная температура = {maximum_temperature(temperature_l1st)}")
print(f"Минимальная температура = {minimum_temperature(temperature_l1st)}")




