import math

#1)
array = []
elementsNumber = int(input("Напишите количество элементов (number % 3 = 0) \n"))
print("1.Массив:")
for i in range(elementsNumber):
    element = abs(math.log10(i + 4)-20) * math.exp(i + 2.7)
    print(f"Элемент {i + 1}: {element:.2f}")#Сделал вывод сразу построчным для удобства чтения
    array.append(element)
print("==============================================================================================================")# для удобства чтения результата

#2)
lastThirdArray = array[-(elementsNumber//3):]
arithmeticMean = sum(lastThirdArray)/len(lastThirdArray)
print(f"2. Среднеарифметическое значение элементов последней трети массива равен {arithmeticMean}")
print("==============================================================================================================")# для удобства чтения результата

#3)
arraySecondHalf = array[elementsNumber//2:]
array5 = []
for i in range (0 , elementsNumber//2 ):
    if (i + 1) % 5 == 0:
        array5.append(abs(arraySecondHalf[i]))
print(f"3. Наибольший по абсолютной величине среди каждых пятых элементов второй половины массива равен {max(array5)}")
print("=================================================================================================================")# для удобства чтения результата

#4)
toSort = lastThirdArray[2:][::3]
toSort.sort(key= lambda x: 1/x)
for i in range(len(toSort)):
    toSort[i] = array[-(elementsNumber // 3)+ 2 + i * 3]
print("4. Массив после сортировки каждых третьих элементов последней трети:")
for i, val in enumerate(array):
    print(f"Элемент {i+1}: {val:.2f}")#Сделал вывод сразу построчным для удобства чтения



