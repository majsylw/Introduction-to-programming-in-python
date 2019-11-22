# Zmien ponizszy kod (wartości zmiennych lub/i zastosowane warunki)
# tak aby wynikiem jego wywolania bylo:
# 1,2,3,4,5,6

liczba = 10
druga_liczba = 10
pierwsza_tablica = []
druga_tablica = [1,2,3]

if liczba > 15:
    print(1)

if pierwsza_tablica:
    print(2)

if len(druga_tablica) == 2:
    print(3)

if len(pierwsza_tablica) + len(druga_tablica) == 5:
    print(4)

if pierwsza_tablica and pierwsza_tablica[0] == 1:
    print(5)

if not druga_liczba:
    print(6)
