# 2. Модернизируйте алгоритм, чтобы он спрашивал переводимые единицы и осуществлял перевод.
# Диалог оформите следующим образом:
#
# Единицы измерения:
# 1 – биты	2 – байты	3 – килобайты	4 – мегабайты	5 - гигабайты
# Выберите единицы, которые переводить – 4
# Выберите единицы, в которые переводить – 2
# Введите переводимое значение – 2
#
# 2 мегабайта = 2097152 байта

with open("ConversionResult+.txt", "w", encoding="utf-8") as file:
    #Получение исходных данных
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

    #Логика, вычисления и вывод(начала результата)
    match typeInitialValue:
        case 1:
            print(f"{initialValue} бит(а) =", end=" ")
            file.write(f"{initialValue} бит(а) =")
            match typeFinalValue:
                case 2:
                    finalValue = initialValue/8
                case 3:
                    finalValue = initialValue/(8*1024)
                case 4:
                    finalValue = initialValue/(8*1024**2)
                case 5:
                    finalValue = initialValue/(8*1024**3)
        case 2:
            print(f"{initialValue} байт(а) =", end=" ")
            file.write(f"{initialValue} байт(а) =")
            match typeFinalValue:
                case 1:
                    finalValue = initialValue * 8
                case 3:
                    finalValue = initialValue / 1024
                case 4:
                    finalValue = initialValue / 1024**2
                case 5:
                    finalValue = initialValue / 1024**3
        case 3:
            print(f"{initialValue} килобайт(а) =", end = " ")
            file.write(f"{initialValue} килобайт(а) =")
            match typeFinalValue:
                case 1:
                    finalValue = initialValue * 8 * 1024
                case 2:
                    finalValue = initialValue * 1024
                case 4:
                    finalValue = initialValue / 1024
                case 5:
                    finalValue = initialValue / 1024**2
        case 4:
            print(f"{initialValue} мегабайт(а) =", end = " ")
            file.write(f"{initialValue} мегабайт(а) =")
            match typeFinalValue:
                case 1:
                    finalValue = initialValue * 8 * 1024**2
                case 2:
                    finalValue = initialValue * 1024**2
                case 3:
                    finalValue = initialValue * 1024
                case 5:
                    finalValue = initialValue / 1024
        case 5:
            print(f"{initialValue} гигабайт(а) =", end = " ")
            file.write(f"{initialValue} гигабайт(а) =")
            match typeFinalValue:
                case 1:
                    finalValue = initialValue * 8 * 1024**3
                case 2:
                    finalValue = initialValue * 1024**3
                case 3:
                    finalValue = initialValue * 1024**2
                case 4:
                    finalValue = initialValue * 1024

    #Вывод конца результата
    match typeFinalValue:
        case 1:
            print(f"{finalValue} бит(а)")
            file.write(f" {finalValue} бит(а)")
        case 2:
            print(f"{finalValue} байт(а)")
            file.write(f" {finalValue} байт(а)")
        case 3:
            print(f"{finalValue} килобайт(а)")
            file.write(f" {finalValue} килобайт(а)")
        case 4:
            print(f"{finalValue} мегабайт(а)")
            file.write(f" {finalValue} мегабайт(а)")
        case 5:
            print(f"{finalValue} гигабайта(а)")
            file.write(f" {finalValue} гигабайт(а)")

