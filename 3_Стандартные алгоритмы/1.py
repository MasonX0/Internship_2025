


#Счет
print("Введите количество товарных единиц: ",end="")
CommodityUnit=int(input())
ListOfCommodyNames=[]
ListOfCommodyPrices=[]
SummOfPurchase=0
for i in range(CommodityUnit):
    print("Цена товара {0} (руб.): ".format(1+i),end="")
    ListOfCommodyNames.append(float(input()))
    print("Количество товара {} (шт.): ".format(1+i), end="")
    ListOfCommodyPrices.append(int(input()))
    SummOfPurchase+=ListOfCommodyPrices[i]*ListOfCommodyNames[i]
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
print("Дата 26.07.2039")
print("Кассир Мавлетбердин М.А.\n")
for i in range(CommodityUnit):
    print("Товара №{0} {1}шт.* {2} (руб.): {3}".format((1+i),int(ListOfCommodyNames[i]),float(ListOfCommodyPrices[i]),float(ListOfCommodyPrices[i]*ListOfCommodyNames[i])))
print("\tСтоимость покупки: {0} руб.".format(SummOfPurchase))
print("\tСкидка	{0}% : {1} ".format(int(Discount),SummOfPurchase*Discount))
print("\tИТОГО К ОПЛАТЕ   {0} руб.".format(SummOfPurchase))

# Введите количество товарных единиц: 2
# Цена  товара1(руб.):  2.75
# Количество товара1(шт.): 5
# Цена товара2 (руб.): 0.85
# Количество товара2(шт): 2
#
# 	Стоимость покупки: 15.45 руб.
#
#  Предусмотрите печать чека в файл в виде:
# Дата 25.06.2014
# Кассир Иванова И.П.
#
# Товар1	5 шт.* 2.75		13.75
# Товар2	2 шт.* 0.85		1.70
#
# ИТОГО К ОПЛАТЕ			15.45 руб.
