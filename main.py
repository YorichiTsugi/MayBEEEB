from random import randint
spisok = []
i = 0
polz = 0
otrz = 0
print("Сколько чисел хош?")
itachi = int(input())
while len(spisok) != itachi:
    a = randint (-100, 100)
    if a == 0:
        a = randint (-100, 100)
    else:
        spisok.append(a)
while i < len(spisok):
    if spisok[i] > 0:
        polz = polz + spisok[i]
        i += 1
    elif spisok[i] < 0:
        otrz = otrz + spisok[i]
        i += 1
print('Вот все твои циферки или числа, не знаю', spisok)
print('А вот сумма всех положительных = ', polz)
print('Ну и сумма отрицательных тоже = ', otrz)