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

Napisz program, ktory w funkcji porownuje dwie liczby calkowite:
a i b. Jesli a jest wieksze od b funkcja zwraca wartosc 1, jesli b
jest wieksze od a zwraca -1, a jesli liczby sa rowne funkcja
zwraca 0. Wywołanie tej funkcji powinno znajdowac sie w funkcji main.
Liczby a i b powinne byc podane przez uzytkownika.
Wynik wyświetlaj w funkcji main w stosownym formacie.
'''

def zliczanie(a,b): # 1pkt
    if a>b: # 1
        return 1 #1
    elif b>a: #1
        return -1 #1
    else: #1
        return 0 #1


def main():
    c = input("Podaj liczbe a: ") # 1
    z = input("Podaj liczbe b: ") # 1

    print("Funkcja zwróci 1, jeśli a jest większe od b\nFunkcja zwróci -1, jeśli b jest większe od a\nFunkcja zwróci 0, jeśli a jest równe b")
    print("Wynikiem jest: ",zliczanie(c,z)) # 1

main()
