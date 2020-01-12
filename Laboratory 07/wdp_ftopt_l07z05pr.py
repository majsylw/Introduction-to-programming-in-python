# Zmien ponizszy kod tak aby wynikiem jego wywolania
# bylo:
# 1,2,3,4,5,6

liczba = 10
druga_liczba = 10
pierwsza_tablica = []
druga_tablica = [1,2,3]

# zmiana warunku, bo 10 jest mniejsze od 15, zmiana znaku na końcu wypisywanej linii przez funkcję print
if liczba < 15:
    print(1,end=",")
# pierwsza_tablica jest pusta więc zwraca false, musimy zaprzeczyć warunkowi
if not pierwsza_tablica:
    print(2, end=",")
# w drugiej_tablicy są 3 elementy
if len(druga_tablica) != 2:
    print(3,end=",")
# w pierwszej tablicy nie ma elementów, a w drugiej są 3, więc ich suma wynosi 3
if len(pierwsza_tablica) + len(druga_tablica) != 5:
    print(4,end=",")
# pierwsza_tablica jest pusta, a pierwszym elementem druga_tablica jest 1
if not pierwsza_tablica and druga_tablica[0] == 1:
    print(5,end=",")
# druga liczba jest różna od 0
if druga_liczba:
    print(6)
