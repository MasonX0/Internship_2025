# Написать программу, вычисляющую количество учащихся группы, чей максимальный балл за семестр ниже среднего.
# Успеваемость вводится в массив данных в процессе работы программы в виде последовательности оценок каждого студента,
# последовательность заканчивается значением -1. Формирование массива заканчивается -2.
# Предусмотреть выбор ввода данных с клавиатуры или из файла.

students_list = []
choice = int(input("Укажите тип ввода данных:\n1 — с клавиатуры    2 — из файла\n"))
if choice > 2:
    raise print("Перезапустите программу и напишите число 1 или 2")
match choice:
    case 1:
        print("Введите баллы каждого учащегося:\n(Для прекращения заполнения баллов студента — '-1'\nДля прекращения заполнения студентов — '-2')")
        students_number = 1
        while True:
            print(f"Студент {students_number}: ")
            students_number += 1
            students_scores = []
            while True:
                score = int(input())
                students_scores.append(score)
                if score == -1 or score == -2:
                    students_scores = students_scores[:-1]
                    break
            students_list.append(students_scores)
            if score == -2:
                break
    case 2:
        with open ("Read+++.txt", "r+", encoding="utf-8") as file:
            line = "none"
            while line != "":
                line = file.readline()
                if line == "":
                    break
                line = list(map(int, line.split(sep = " ")))
                students_list.append(line)


amount_of_points = 0
scores_count = 0
list_of_maximum_students_scores = []
for _ in students_list:
    students_amount_of_points = sum(_)
    students_scores_count = len(_)
    list_of_maximum_students_scores.append(max(_))
    amount_of_points += students_amount_of_points
    scores_count += students_scores_count

average_score = amount_of_points/scores_count
below_average_count = len([x for x in list_of_maximum_students_scores if x < average_score])
print(f"{below_average_count} — количество учащихся группы, чей максимальный балл за семестр ниже среднего")








