# Две строки
name_cyr = "Хайруллин Динар"
name_lat = "Khayrullin Dinar"

# Открываем файл для записи
with open("output.txt", "w", encoding="utf-8") as f:
    # Функция для обработки и записи информаци
    def write_info(name, title):
        f.write(f"{title}\n")

        # Юникод (десятичный)
        unicode_dec = [str(ord(c)) for c in name]
        f.write("Юникод (десятичный): " + " ".join(unicode_dec) + "\n")

        # Юникод (шестнадцатеричный)
        unicode_hex = [hex(ord(c))[2:].upper().zfill(4) for c in name]
        f.write("Юникод (шестнадцатеричный): " + " ".join(unicode_hex) + "\n")

        # ASCII (если возможно)
        if all(ord(c) < 128 for c in name):
            ascii_dec = [str(ord(c)) for c in name]
            ascii_hex = [hex(ord(c))[2:].upper().zfill(2) for c in name]
            f.write("ASCII (десятичный): " + " ".join(ascii_dec) + "\n")
            f.write("ASCII (шестнадцатеричный): " + " ".join(ascii_hex) + "\n")
        else:
            f.write("ASCII: Недоступно (есть не-ASCII символы)\n")

        f.write("\n")  # пустая строка между блоками


    # Обрабатываем обе строки
    write_info(name_cyr, "Хайруллин Динар")
    write_info(name_lat, "Khayrullin Dinar")

print("Файл 'output.txt' успешно создан!")