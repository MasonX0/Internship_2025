#1. Напишите программу перевода мегабайтов в биты, байты, килобайты, гигабайты.
# Результаты выводить на экран и в файл.
with open ("ConversionResult.txt", "w", encoding='utf-8') as file:
   megabytesNumber = int(input("Введите количество мегабайтов: "))
   bits = megabytesNumber * 8388608
   bytes = megabytesNumber * 1048576
   kilobytes = megabytesNumber * 1024
   gigabytes = megabytesNumber / 1024
   print(f"{megabytesNumber} мегабайт(а) равны: {bits} битам, {bytes} байтам, {kilobytes} килобайтам, {gigabytes} гигабайтам")
   file.write(f"{megabytesNumber} мегабайт(а) равны: {bits} битам, {bytes} байтам, {kilobytes} килобайтам, {gigabytes} гигабайтам")
