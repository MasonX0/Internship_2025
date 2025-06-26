# Написать программу, вычисляющую количество учащихся группы, чей рост выше среднего.
# Рост вводится в массив данных в процессе работы программы, последовательность заканчивается значением 0.
# Предусмотреть выбор ввода данных с клавиатуры или из файла.

choice = int(input("Укажите тип ввода данных\nс клавиатуры — 1   из файла — 2\n"))
if choice > 2:
    raise ValueError("неверное значение!")
if choice == 1:
    i = 1
    height_of_students = []
    print("Если надо остановиться — введите 0")
    while True:
        height_of_student = float(input(f"Введите рост {i} учащегося(в см): "))
        if height_of_student == 0.0:
            break
        height_of_students.append(height_of_student)
        i += 1

else:
    with open("Read+.txt", "r", encoding="utf-8") as file:
        height_str = file.read()
        height_list_str = height_str.split(sep=" ")
        height_of_students = list(map(float, height_list_str))
        print(f"Рост учащихся(из файла):\n{height_of_students}")

average_height = sum(height_of_students) / len(height_of_students)
c0unt = 0
for h in  height_of_students:
    if h > average_height:
        c0unt += 1

print(f"{c0unt} — количество учащихся группы, чей рост выше среднего")




