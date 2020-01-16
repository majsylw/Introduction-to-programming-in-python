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
Napisz program, ktory zlicza ile razy dana litera wystepuje
w podanym ciagu znakow. Zliczanie powinno byc wykonane w funkcji.
Funkcja ta ma przyjmować 2 argumenty - zadany ciąg znaków oraz znak,
którego wystąpnie w ciągu chcemy zliczyć. Funkcja ma zwrócić
liczbę wystapien danego znaku.
Wywołanie funkcji zliczającej ile razy występuje pewien znak umieść w funkcji main(),
zarówno ciąg znaków, jak i zliczany znak powinny zostać wprowadzone przez użytkownika z klawiatury.
Wynik wyświetl w funkcji main w stosownym formacie.
'''

def zliczanie(ciag,znak): # 1pkt
    licz = 0 # 1
    for i in ciag: # 2
        if i==znak: # 1
            licz+=1 # 1
    return licz # 1


def main():
    c = input("Podaj ciag zniakow: ") # 1
    z = input("Jaki znak bedziemy zliczac? ") # 1

    print("Liczba wystapien",zliczanie(c,z)) # 1

main()
