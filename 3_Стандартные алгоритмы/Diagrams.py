from pyflowchart import Flowchart

code = """
while isRepeat == True:
    print("Единицы измерения:")
    print("1 – миллиметры	2 – сантиметры	3 – дециметры	4 – метры	5 - километры\\n")

    print("Выберите единицы, которые переводить - ", end="")
    TranslateFrom = float(input())

    print("Выберите единицы, в которые переводить - ", end="")
    TranslateTo = float(input())

    print("Введите переводимое значение - ", end="")
    value = float(input())

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

    print("Ваш перевод - ", end="")
    YourAnswer = float(input())

    if YourAnswer == trans:
        count += 1

    print("Продолжить? (y/n) ", end="")
    isContinue = input()
    print("")

    while isContinue != "n" and isContinue != "y":
        print("Внимательнее!")
        print("Продолжить? (y/n) ", end="")
        isContinue = input()
        print("")

    if isContinue == "n":
        isRepeat = False
        print("ВЕРНЫХ ОТВЕТОВ - {}".format(count))
        print("УДАЧИ!")
"""

fc = Flowchart.from_code(code)
print(fc.flowchart())  # Вывод в формате Mermaid.js