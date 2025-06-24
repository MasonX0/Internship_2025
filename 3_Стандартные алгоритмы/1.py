
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
if (300<SummOfPurchase < 500.0):
    Discount = 0.03
    SummOfPurchaseWithDiscount=SummOfPurchase * (1-Discount)
elif (500.0<SummOfPurchase < 1000.0):
    Discount = 0.05
    SummOfPurchaseWithDiscount=SummOfPurchase * (1-Discount)
elif (SummOfPurchase > 1000.0):
    Discount = 0.10
    SummOfPurchaseWithDiscount=SummOfPurchase * (1-Discount)
else :
    Discount = 0.0
    SummOfPurchaseWithDiscount = SummOfPurchase * (1 - Discount)


print("\n\tСтоимость покупки: {0} руб.".format(SummOfPurchase))
print("\tСКИДКА: {0}%".format(int(Discount)))
print("\tИТОГ: {0} руб.\t".format(SummOfPurchaseWithDiscount))

#Чек
print("\n\n\n\nВАШ ЧЕК")
print("Дата 14.04.2035")
print("Кассир Мавлетбердина А.А.\n")
print("Тетрадь	{0} шт.* {1}		{2}".format(PriceOfNotebook,CountOfNotebook,PriceOfNotebook*CountOfNotebook))
print("Карандаш	{0} шт.* {1}		{2}\n".format(PriceOfPencil,CountOfPencil,PriceOfPencil*CountOfPencil))
print("\tСтоимость покупки: {0} руб.".format(SummOfPurchase))
print("\tСкидка	{0}% : {1} ".format(int(Discount),SummOfPurchase*Discount))
print("\tИТОГО К ОПЛАТЕ   {0} руб.".format(SummOfPurchase))

# Цена тетради (руб.):  2.75
# Количество тетрадей (шт.): 150
# Цена карандаша (руб.): 0.85
# Количество карандашей (шт): 25
#
# 	Стоимость покупки: 433.75 руб.
# 	СКИДКА 3%:	13.01
# 	ИТОГ:	420.74 руб.
#
#  Предусмотрите печать чека в файл в виде:
# Дата 30.06.2015
# Кассир Иванова И.П.
#
# Тетрадь	150 шт.* 2.75		412.5
# Карандаш	25 шт.* 0.85		21.25
#
#
# Стоимость покупки: 433.75 руб.
# 	СКИДКА 3%:	13.01
#
# ИТОГО К ОПЛАТЕ	420.74 руб.
