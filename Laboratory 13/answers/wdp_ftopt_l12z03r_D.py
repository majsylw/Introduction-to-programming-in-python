"""
Wstep do programowania
Kolokwium termin 0
9.01.2019 grupa P11-57j
imie:
nazwisko:
indeks:
"""

'''
Zadanie 3 (10 pkt.)
Napisz program, ktory dla podanej przez użytkownika liczby rzeczywistej zwróci jej część ułamkową.
W tym celu zdefiniuj funkcje czesc_ulamkowa, ktora zwraca czesc ulamkowa liczby
rzeczywistej podanej jako jej argument.
Wywołanie funkcji czesc_ulamkowa() umieść w funkcji main(),
rozważana liczba rzeczywista powinna zostać wprowadzona przez użytkownika z klawiatury.
Wynik wyświetl w funkcji main zaokrąglając go do 4 miejsc po przecinku.
'''

def czesc_ulamkowa(liczba): # 2
    return liczba - int(liczba) # 3

def main():
    n = float(input("Podaj liczbe rzeczywista: ")) # 2

    wynik = czesc_ulamkowa(n) # 1
    print("Czesc ulamkowa podanej liczby rzeczywistej wynosi: ", format(wynik,".4f")) # 2

main()
