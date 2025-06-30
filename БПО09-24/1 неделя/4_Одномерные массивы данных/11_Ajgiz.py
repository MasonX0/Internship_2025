
array = []
print("Введите количество элементов массива: ",end="")
count=int(input())

# Part_1
for i in range(1,count+1):
    array.append(pow(4.5-i,(i/1)))
print("Ваш массив: {}".format(array))

# Part_2 Вычислить сумму каждых вторых элементов второй половины массива
Sum=0
# # Вторая половина без учета середины (в нечетных случаях)
for i in range(int(len(array)/2+0.5)+1,int(len(array)),2):
    Sum+=array[i]
print("Сумма каждых вторых элементов второй половины массива: {}".format(Sum))

# Part_3 Определить наименьший элемент среди ненулевых элементов второй четверти массива

# # Вторая четверть включает серединный элемент (в нечетных случаях), в len(array)%4!=0 случаях она меньше чем первая
minEl=array[int(len(array)/4+0.5)]
for i in range( int(len(array)/4+0.5),int(len(array)/2+0.5)):
    if array[i]<minEl and array[i]!=0:
        minEl=array[i]
print("Наименьший элемент среди ненулевых элементов второй четверти массива: {}".format(minEl))

# Part_4 Упорядочить ненулевые элементы всего массива по возрастанию абсолютных значений

# # Вообще, посмотрев на условие заполнения элементов массива, ясно, что все элементы НЕнулевые, но все же
intermediary=0
for i in range(len(array)):
    for j in range(len(array)):
        if (abs(array[i])<abs(array[j]))and array[i]!=0 and array[j]!=0:
            intermediary=array[j]
            array[j]=array[i]
            array[i]=intermediary
print("Все НЕнулевые элементы массива упорядочены по возрастанию абсолютных значений: \n{}".format(array))