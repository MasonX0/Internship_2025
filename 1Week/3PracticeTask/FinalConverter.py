# 3. Доработайте предыдущий алгоритм так, чтобы система проверяла умение пользователя переводить единицы измерения. Предусмотрите многократную проверку перевода с подсчётом правильных ответов.
# Единицы измерения:
# 1 – биты	2 – байты	3 – килобайты	4 – мегабайты	5 - гигабайты
# Выберите единицы, которые переводить  – 4
# Выберите единицы, в которые переводить – 2
# Введите переводимое значение – 2
#
# Ваш перевод - 2097152
# Продолжить? (y/n) n
#
# ВЕРНЫХ ОТВЕТОВ – 1
# УДАЧИ!
from os import write

with open("ConversionResult++.txt", "w", encoding="utf-8") as file:
    cont1nue = True
    rightAnswer = 0

    while cont1nue:
        print("Единицы измерения:")
        file.write("Единицы измерения:\n")
        print("1 – биты	2 – байты 3 – килобайты	4 – мегабайты 5 - гигабайты")
        file.write("1 – биты	2 – байты 3 – килобайты	4 – мегабайты 5 - гигабайты\n")
        typeInitialValue = int(input("Выберите единицы, которые переводить – "))
        file.write(f"Выберите единицы, которые переводить – {typeInitialValue}\n")
        typeFinalValue = int(input("Выберите единицы, в которые переводить – "))
        file.write(f"Выберите единицы, в которые переводить – {typeFinalValue}\n")
        initialValue = float(input("Введите переводимое значение – "))
        file.write(f"Введите переводимое значение – {initialValue}\n")
        print("\n", end="")
        file.write("\n")

        # Логика, вычисления и вывод(начала результата)
        match typeInitialValue:
            case 1:
                match typeFinalValue:
                    case 2:
                        finalValue = initialValue / 8
                    case 3:
                        finalValue = initialValue / (8 * 1024)
                    case 4:
                        finalValue = initialValue / (8 * 1024 ** 2)
                    case 5:
                        finalValue = initialValue / (8 * 1024 ** 3)
            case 2:
                match typeFinalValue:
                    case 1:
                        finalValue = initialValue * 8
                    case 3:
                        finalValue = initialValue / 1024
                    case 4:
                        finalValue = initialValue / 1024 ** 2
                    case 5:
                        finalValue = initialValue / 1024 ** 3
            case 3:
                match typeFinalValue:
                    case 1:
                        finalValue = initialValue * 8 * 1024
                    case 2:
                        finalValue = initialValue * 1024
                    case 4:
                        finalValue = initialValue / 1024
                    case 5:
                        finalValue = initialValue / 1024 ** 2
            case 4:
                match typeFinalValue:
                    case 1:
                        finalValue = initialValue * 8 * 1024 ** 2
                    case 2:
                        finalValue = initialValue * 1024 ** 2
                    case 3:
                        finalValue = initialValue * 1024
                    case 5:
                        finalValue = initialValue / 1024
            case 5:
                match typeFinalValue:
                    case 1:
                        finalValue = initialValue * 8 * 1024 ** 3
                    case 2:
                        finalValue = initialValue * 1024 ** 3
                    case 3:
                        finalValue = initialValue * 1024 ** 2
                    case 4:
                        finalValue = initialValue * 1024

        usersValue = int(input("Ваш перевод - "))
        file.write(f"Ваш перевод - {usersValue}\n")
        if usersValue == finalValue:
            rightAnswer += 1

        programContinue = input("Продолжить? (y/n)\n")
        file.write(f"Продолжить? (y/n)\n{programContinue}\n")
        a = True
        while a:
            if programContinue == "n":
                cont1nue = False
                a = False
            elif programContinue == "y":
                a = False
            else:
                print("Только 'y' или 'n'")
                file.write("Только 'y' или 'n'\n")
                programContinue = input("Продолжить? (y/n)\n")
                file.write(f"Продолжить? (y/n)\n{programContinue}\n")


    print(f"ВЕРНЫХ ОТВЕТОВ – {rightAnswer}\nУДАЧИ!")
    file.write(f"ВЕРНЫХ ОТВЕТОВ – {rightAnswer}\nУДАЧИ!")
