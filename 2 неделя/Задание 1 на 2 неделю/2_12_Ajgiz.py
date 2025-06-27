import re
wordsOnLines=[]
Lists=[]
L1=[]
consonants = 'бвгджзйклмнпрстфхцчшщъьБВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ'
def cntconsonants (i):
    return sum(i.count(c) for c in consonants)
with open('stringsINPUT.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip("\n") for line in file]
    cnt=0
    for i in lines:
        cnt+=1
        L2 = []
        L2.append(f"{cnt}. ") #!!!!!!
        for j in i.split(" "):
            if cntconsonants(j)%2!=0:
                L2.append(f"{j} ")
        if len(L2)>1:
            L1.append(L2)
print(L1)
with open('stringsOUTPUT.txt', 'w', encoding='utf-8') as file:
    for i in L1:
        file.write(("".join([j for j in i])+"\n"))
