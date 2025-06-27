import numpy as np

# Part 1 Temperature

choice = int(input("1 - ввод с клавиатуры, 2 - автозаполнение, 3 - с файла : "))
if choice == 1:
    recruitedList = input("Введите числа через пробел: ")
    listOfTemperatures = list(map(float, recruitedList.split()))
elif choice == 2:
    listOfTemperatures = np.random.uniform(low=15, high=35, size=7)
elif choice == 3:
    listOfTemperatures = np.loadtxt("data_Ajgiz.txt")
else:
    listOfTemperatures = np.random.uniform(low=15, high=35, size=7)
def AverageTemperature(list):
    av = sum(list) / len(list)
    return av
def MaxTemperature(list):
    mx = max(list)
    return mx
def MinTemperature(list):
    mn = min(list)
    return mn

print("Ваш список температур за неделю: ", listOfTemperatures)
print("Min за неделю: ", MinTemperature(listOfTemperatures))
print("Max за неделю: ", MaxTemperature(listOfTemperatures))
print("Average за неделю: ", AverageTemperature(listOfTemperatures))



