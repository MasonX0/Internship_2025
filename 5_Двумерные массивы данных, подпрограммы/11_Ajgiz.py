import numpy as np


#Создаем матрицу
print("Размер квадратной матрицы: ",end='')
sIze= int(input())
np.random.seed(1208)
matrix = np.random.rand(sIze, sIze)
print("Ваша матрица: \n{} ".format(matrix))


# a) формирования на его основе одномерного массива Vk – сумма элементов k-той строки и k-того столбца;
def A(matrix):
    Vk=[]
    for i in range(sIze):
        s=0
        for j in range(sIze):
            s+=(float(matrix[i,j]))

        Vk.append(s)

    return Vk

PartA=A(matrix)
print("Ваш вектор Vk: ",A(matrix))

# б) транспонировать матрицу (MT);

def B(matrix):
    Tmatrix = matrix.T
    return Tmatrix


PartB=B(matrix)
print("Ваш транспонировананя матрица: \n",B(matrix))

# в) V MT.

def C(Vk,Tmatrix):
    multiplication = Vk*Tmatrix
    return  multiplication


PartС= C(PartA,PartB)
print("Результат: \n",PartС)



#  Напишите алгоритм формирования и вывода элементов двумерного массива данных (целочисленной матрицы Мn  m) генератором псевдослучайных чисел с последующим вызовом к нему функций
# а) формирования на его основе одномерного массива (вектора V) по определённому правилу;
# б) преобразования самой матрицы М*;
# в) матричной операции над вектором (V) и матрицей (M или М*).
#
# n = m – квадратная матрица.
# а) Vk – сумма элементов k-той строки и k-того столбца;
# б) транспонировать матрицу (MT);
# в) V MT.
