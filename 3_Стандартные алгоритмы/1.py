PriceOfNotebook=2.75
PriceOfPencil=0.85
#Счет
print("Цена тетради (руб.): 2.75")
print("Количество тетрадей (шт.): ",end="")
CountOfNotebook=int(input())
print("Цена карандаша (руб.):  0.85")
print("Количество карандашей (шт): ",end="")
CountOfPencil=int(input())
SummOfPurchase = PriceOfPencil*CountOfPencil + PriceOfNotebook*CountOfNotebook
print("\n\tСтоимость покупки: ",SummOfPurchase)

#Чек
print("\n\n\n\nВАШ ЧЕК")
print("Дата 08.12.2006")
print("Кассир Ахметшина А.И\n")
print("Тетрадь	{0} шт.* {1}		{2}".format(PriceOfNotebook,CountOfNotebook,PriceOfNotebook*CountOfNotebook))
print("Карандаш	{0} шт.* {1}		{2}\n".format(PriceOfPencil,CountOfPencil,PriceOfPencil*CountOfPencil))
print("ИТОГО К ОПЛАТЕ			{0}.".format(SummOfPurchase))

