# Написать программу, которая возвращает номер общежития, в котором есть наиболее заселенный этаж.
# Входные данные (число проживающих в комнате) находятся в трехмерном массиве M[i][j][k],
# где i - номер общежития, j - номер этажа, k - номер комнаты.
# Предусмотреть выбор ввода данных с клавиатуры или из файла.

choice = int(input("Укажите тип ввода данных\n1 — с клавиатуры   2 — из файла\n"))
if choice != 1 and choice != 2:
    raise print("Перезапустите программу и введите цифру 1 или 2")
array_of_dormitories = []
match choice:
    case 1:
        number_of_dormitories = int(input("Введите количество общежитий:\n"))
        dormitories_number = 1
        for _ in range(number_of_dormitories):
            number_of_floors = int(input(f"Введите количество этажей в общежитии №{dormitories_number}: "))
            number_of_rooms_on_the_floor = int(input("Введите количество комнат на этаже: "))
            number_of_rooms = number_of_rooms_on_the_floor * number_of_floors
            print("Введите количество жителей в каждой комнате")
            rooms_number = 1
            people_in_dormitories = []
            floors_number = 1
            for floor in range(number_of_floors):
                print(f"Этаж {floors_number}")
                people_in_floor = []
                for room in range(number_of_rooms_on_the_floor):
                    people_in_room = int(input(f"Комната {rooms_number}: "))
                    people_in_floor.append(people_in_room)
                    rooms_number += 1
                people_in_dormitories.append(people_in_floor)
                floors_number += 1
            array_of_dormitories.append(people_in_dormitories)
            dormitories_number += 1

    case 2:
        with open("Read++++.txt", "r", encoding="utf-8") as file:
            number_of_dormitories = int(file.readline())
            for _ in range(number_of_dormitories):
                number_of_floors = int(file.readline())
                number_of_rooms_on_the_floor = int(file.readline())
                people_in_dormitories = []
                for _ in range(number_of_floors):
                    people_in_floor = list(map(int, file.readline().split()))
                    people_in_dormitories.append(people_in_floor)
                array_of_dormitories.append(people_in_dormitories)


max_residents = -1
result_dormitory = -1
result_floor = -1

for dormitory_idx, dormitory in enumerate(array_of_dormitories, 1):
    for floor_idx, floor in enumerate(dormitory, 1):
        total_residents = sum(floor)
        if total_residents > max_residents:
            max_residents = total_residents
            result_dormitory = dormitory_idx
            result_floor = floor_idx

print(f"Наиболее заселенный этаж находится в общежитии №{result_dormitory}")
print(f"Это этаж №{result_floor} с {max_residents} жителями")