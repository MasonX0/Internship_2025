# В массиве хранятся фамилии с инициалами учеников класса (Иванов П.П.).
# Требуется напечатать список класса с указанием для каждого ученика количества его однофамильцев.

list_of_initials = input("Введите инициалы учеников через запятую:\n").split(sep=", ")
list_of_surnames = []
for initial in list_of_initials:
    surname_str = ""
    for symbol in initial:
        if symbol != " ":
            surname_str += symbol
        else:
            break
    list_of_surnames.append(surname_str)

for index in range(len(list_of_surnames)):
    print(f"{(list_of_surnames.count(list_of_surnames[index]))- 1} — число однофамильцев у ученика с инициалами {list_of_initials[index]}")



