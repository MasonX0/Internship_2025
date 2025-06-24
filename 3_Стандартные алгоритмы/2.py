
print("Единицы измерения:")
print("1 – миллиметры	2 – сантиметры	3 – дециметры	4 – метры	5 - километры\n")
print("Выберите единицы, которые переводить - ",end="")
TranslateFrom = float(input())
print("Выберите единицы, в которые переводить - ",end="")
TranslateTo = float(input())
print("Введите переводимое значение - ",end="")
value = float(input())
if TranslateFrom==1:
    ToName = "миллиметра"
elif TranslateFrom==2:
    ToName = "сантиметра"
elif TranslateFrom==3:
    ToName = "дециметра"
elif TranslateFrom==4:
    ToName = "метра"
elif TranslateFrom==5:
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

if (TranslateTo!=5 and TranslateFrom!=5):
    if (abs(TranslateFrom - TranslateTo) == 2) :
        if TranslateFrom > TranslateTo:
            trans = int(value * 100)
        else:
            trans = value/100
    elif (abs(TranslateFrom - TranslateTo) == 3):
        if TranslateFrom > TranslateTo:
            trans = int(value * 1000)
        else:
            trans = value / 1000
    elif (abs(TranslateFrom - TranslateTo) == 1):
        if TranslateFrom > TranslateTo:
            trans = int(value * 10)
        else:
            trans = value / 10

    else:
        trans=value
else:
    if (abs(TranslateFrom - TranslateTo) == 2):
        if TranslateFrom > TranslateTo:
            trans = int(value * 10000)
        else:
            trans = value / 10000
    elif (abs(TranslateFrom - TranslateTo) == 3):
        if TranslateFrom > TranslateTo:
            trans = int(value * 100000)
        else:
            trans = value / 100000
    elif (abs(TranslateFrom - TranslateTo) == 4):
        if TranslateFrom > TranslateTo:
            trans = int(value * 1000000)
        else:
            trans = value / 1000000
    elif (abs(TranslateFrom - TranslateTo) == 1):
        if TranslateFrom > TranslateTo:
            trans = int(value * 1000)
        else:
            trans = value / 1000
    else:
        trans=value

print("{} {} = {} {}".format(value,ToName[:-1],trans,TransName[:-1]+"ов"))

with open('2.txt', 'r+', encoding='utf-8') as f:
    f.write("{} {} = {} {}\n".format(value,ToName[:-1],trans,TransName[:-1]+"ов"))


# Единицы измерения:
# 1 – миллиметры	2 – сантиметры	3 – дециметры	4 – метры	5 - километры
# Выберите единицы, которые переводить  – 4
# Выберите единицы, в которые переводить – 2
# Введите переводимое значение – 1.23
#
# 1.23 метра = 123 сантиметра

