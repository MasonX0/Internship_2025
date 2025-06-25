# Напишите алгоритм формирования и вывода элементов двумерного массива данных
# (целочисленной матрицы Мn  m) генератором псевдослучайных чисел с последующим вызовом к нему функций
# а) формирования на его основе одномерного массива (вектора V) по определённому правилу;
# б) преобразования самой матрицы М*;
# в) матричной операции над вектором (V) и матрицей (M или М*).
#
# 22 вариант.
# а) Vk - сумма элементов k-строки матрицы;
# б) умножить матрицу на третий элемент вектора;
# в) каждый столбец матрицы сложить с вектором V.
import random as rm

#a)
def vector(matrix):
    vect0r = []
    for k in range(rows):
        summ = 0
        for i in range(cols):
            summ += matrix[k][i]
        vect0r.append(summ)
    return vect0r

#б)
def multiplication(matrix, vector):
    third_element = vector[2]
    multiplied_matrix = [[x * vector[2] for x in row] for row in matrix]
    return multiplied_matrix


rows = int(input("Введите количество строк:"))
cols = int(input("Введите количество столбцов:"))
matrixGlobal = [[rm.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

print("Ваша матрица:")
for k in range(rows):
    for i in range(cols):
        print(f"{matrixGlobal[k][i]}\t", end = " ")
    print("\n", end="")

vectorGlobal = vector(matrixGlobal)
multipliedMatrixGlobal = multiplication(matrixGlobal, vectorGlobal)
print(f"a) Вектор V = {vectorGlobal}")
print("б) Умноженная матрица:")
for k in range(rows):
    for i in range(cols):
        print(f"{multipliedMatrixGlobal[k][i]}\t", end = " ")
    print("\n", end="")

