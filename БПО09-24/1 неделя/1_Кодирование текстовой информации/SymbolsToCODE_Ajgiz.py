
text = "AjgizMavletberdin"
print("Unicode code points (EN):")
for char in text:
    print(f"U+{ord(char):04X}", end=' ')
print("")

text1 = "АйгизМавлетбердин"
print("Unicode code points (RU):")
for char1 in text1:
    print(f"U+{ord(char1):04X}", end=' ')
print("")

print("Ascii code points (EN) :")
text = "AjgizMavletberdin"
ascii = text.encode('ascii')
codes = list(ascii)
print(codes)

