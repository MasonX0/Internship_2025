with open('Mas0n.txt', 'w', encoding='utf-8') as file:
    # Мавлетбердин_And_Айгиз_From_UTF-16_LE
    file.write(
        '\u0410\u0439\u0433\u0438\u0437 \u041C\u0430\u0432\u043B\u0435\u0442\u0431\u0435\u0440\u0434\u0438\u043D \t  RU_From_UTF-16_LE\n')

    #Mavletberdin_And_Ajgiz_From_UTF-16_LE
    file.write(
        '\u0041\u0079\u0067\u0069\u007A \u004D\u0061\u0076\u006C\u0065\u0074\u0062\u0065\u0072\u0064\u0069\u006E \t  EN_From_UTF-16_LE\n')
    #Mavletberdin_And_Ajgiz_From_ASCII
    file.write(
        chr(65) + chr(121) + chr(103) + chr(105)  + chr(122) + ' ' +
        chr(77) + chr(97) + chr(118) + chr(108) + chr(101) + chr(116) +
        chr(98) + chr(101) + chr(114) + chr(100) + chr(105) + chr(110) +
        ' \t  EN_From_ASCII\n'
    )