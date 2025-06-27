isRepeat = True
count = 0
with open('2.3.txt', 'w', encoding='utf-8') as f:
    while isRepeat == True:
        f.write("\n")
        print("Единицы измерения:")
        f.write("Единицы измерения:")

        print("1 – миллиметры	2 – сантиметры	3 – дециметры	4 – метры	5 - километры\n")
        f.write("1 – миллиметры	2 – сантиметры	3 – дециметры	4 – метры	5 - километры\n")
        print("Выберите единицы, которые переводить - ", end="")
        f.write("Выберите единицы, которые переводить - ")
        TranslateFrom = float(input())
        f.write(str(TranslateFrom))
        f.write("\n")
        print("Выберите единицы, в которые переводить - ", end="")
        f.write("Выберите единицы, в которые переводить - ")
        TranslateTo = float(input())
        f.write(str(TranslateTo))
        f.write("\n")
        print("Введите переводимое значение - ", end="")
        f.write("Введите переводимое значение - ")

        value = float(input())
        f.write(str(value))
        f.write("\n")
        if TranslateFrom == 1:
            ToName = "миллиметра"
        elif TranslateFrom == 2:
            ToName = "сантиметра"
        elif TranslateFrom == 3:
            ToName = "дециметра"
        elif TranslateFrom == 4:
            ToName = "метра"
        elif TranslateFrom == 5:
            ToName = "километра"

        if TranslateTo == 1:
            TransName = "миллиметра"
        elif TranslateTo == 2:
            TransName = "сантиметра"
        elif TranslateTo == 3:
            TransName = "дециметра"
        elif TranslateTo == 4:
            TransName = "метра"
        elif TranslateTo == 5:
            TransName = "километра"

        if (TranslateTo != 5 and TranslateFrom != 5):
            if (abs(TranslateFrom - TranslateTo) == 2):
                if TranslateFrom > TranslateTo:
                    trans = (value * 100)
                else:
                    trans = value / 100
            elif (abs(TranslateFrom - TranslateTo) == 3):
                if TranslateFrom > TranslateTo:
                    trans = (value * 1000)
                else:
                    trans = value / 1000
            elif (abs(TranslateFrom - TranslateTo) == 1):
                if TranslateFrom > TranslateTo:
                    trans = (value * 10)
                else:
                    trans = value / 10

            else:
                trans = value
        else:
            if (abs(TranslateFrom - TranslateTo) == 2):
                if TranslateFrom > TranslateTo:
                    trans = (value * 10000)
                else:
                    trans = value / 10000
            elif (abs(TranslateFrom - TranslateTo) == 3):
                if TranslateFrom > TranslateTo:
                    trans = (value * 100000)
                else:
                    trans = value / 100000
            elif (abs(TranslateFrom - TranslateTo) == 4):
                if TranslateFrom > TranslateTo:
                    trans = (value * 1000000)
                else:
                    trans = value / 1000000
            elif (abs(TranslateFrom - TranslateTo) == 1):
                if TranslateFrom > TranslateTo:
                    trans = (value * 1000)
                else:
                    trans = value / 1000
            else:
                trans = value
        f.write("\n")
        f.write("Ваш перевод - ")
        print("Ваш перевод - ", end="")
        YourAnswer = float(input())
        f.write(str(YourAnswer))
        f.write("\n")
        if YourAnswer == trans:
            count += 1
        f.write("\n")
        print("Продолжить? (y/n) ", end="")
        isContinue = input()
        print("")
        f.write("Продолжить? (y/n) :")
        while isContinue != "n" and isContinue != "y":
            print("Внимательнее!")
            print("Продолжить? (y/n) ", end="")
            isContinue = input()
            print("")
        f.write(isContinue)
        f.write("\n")
        f.write("\n")
        if isContinue == "n":
            isRepeat = False
            f.write("ВЕРНЫХ ОТВЕТОВ - {}\n".format(str(count)))
            f.write("УДАЧИ!")
            print("ВЕРНЫХ ОТВЕТОВ - {}".format(count))
            print("УДАЧИ!")


# Единицы измерения:
# 1 – миллиметры	2 – сантиметры	3 – дециметры	4 – метры	5 - километры
#
# Выберите единицы, которые переводить  – 4
# Выберите единицы, в которые переводить – 2
# Введите переводимое значение – 1.23
#
# Ваш перевод - 123
# Продолжить? (y/n)  n
#
# ВЕРНЫХ ОТВЕТОВ – 1
# УДАЧИ!
#  
