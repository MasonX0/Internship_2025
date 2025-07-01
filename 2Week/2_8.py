# Создать программу, позволяющую из одного текстового файла, содержащего несколько строк (тип String)
# текста на русском языке, построчно переписать в другой текстовый файл слова, отвечающие некоторому условию.
# Задания выполнять согласно вариантам.
# Требования:
# – в новом файле следует указать номер строки, в которой искомые слова находились в исходном файле;
# – для каждой строки в конце указать количество выбранных слов.

# Переписать в результирующий файл слова с числом букв больше 5.

with open ("Read.txt", "r", encoding="utf-8") as read_the_file:
    with open("Write.txt", "w", encoding="utf-8") as write_the_file:
        i = 1
        while True:
            line = read_the_file.readline()
            new_line = ""
            if line == "":
                break
            new_line += f"Слова из {i} строки: "
            list_of_line = line.split()
            number_of_words = 0
            for word in list_of_line:
                if len(word) > 5:
                    new_line += word + ", "
                    number_of_words += 1

            if len(new_line) == 19:
                new_line = f"В строке {i} не нашлось подходящих под условие слов\n"
                write_the_file.write(new_line)
            else:
                new_line = new_line[:-2] + "."
                write_the_file.write(f" {new_line}(было выбрано {number_of_words} слов)\n")
            i += 1


