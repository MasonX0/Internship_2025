#Переделанный под мой лад код Айгиза
with open('Decoding.txt', 'w', encoding='utf-8') as file:
    # ХайруллинДинар from UTF-16 LE
    file.write(
        '\u0425\u0430\u0439\u0440\u0443\u043B\u043B\u0438\u043D\u0414\u0438\u043D\u0430\u0440   from UTF-16 LE(RU)\n')

    #KhayrullinDinar from UTF-16 LE
    file.write(
        '\u004B\u0068\u0061\u0079\u0072\u0075\u006C\u006C\u0069\u006E\u0044\u0069\u006E\u0061\u0072  from UTF-16 LE(EN)\n')
    # KhayrullinDinar from ASCII
    file.write(
        chr(75) + chr(104) + chr(97) + chr(121) + chr(114) +
        chr(117) + chr(108) + chr(108) + chr(105) + chr(110) +
        chr(68) + chr(105) + chr(110) + chr(97) + chr(114) +
        '  from ASCII(EN)\n'
    )
