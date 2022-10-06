from random import randint
spis = []
i = 0
polz = 0
otrz = 0
print("Сколько чисел хош?")
itachi = int(input())
while len(spis) != itachi:
    a = randint (-100, 100)
    if a == 0:
        a = randint (-100, 100)
    else:
        spis.append(a)
while i < len(spisok):
    if spis[i] > 0:
        polz = polz + spis[i]
        i += 1
    elif spis[i] < 0:
        otrz = otrz + spis[i]
        i += 1
print('Вот все твои циферки или числа, не знаю', spisok[:])
print('А вот сумма всех положительных = ', polz)
print('Ну и сумма отрицательных тоже = ', otrz)
