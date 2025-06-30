
print("Метры:",end="")
m=float(input())
print("{0} метра = {1} километра".format(float(m),float(m/1000)))
print("{0} метра = {1} дециметра".format(float(m),int(m*10)))
print("{0} метра = {1} сантиметра".format(float(m),int(m*100)))
print("{0} метра = {1} миллиметра".format(float(m),int(m*1000)))
with open('2.1.txt', 'w', encoding='utf-8') as f:
    f.write("{0} метра = {1} километра\n".format(float(m), float(m / 1000)))
    f.write("{0} метра = {1} дециметра\n".format(float(m), int(m*10)))
    f.write("{0} метра = {1} сантиметра\n".format(float(m), int(m * 100)))
    f.write("{0} метра = {1} миллиметра\n".format(float(m), int(m * 1000)))

