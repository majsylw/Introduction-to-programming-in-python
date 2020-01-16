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

Napisz program, ktory dla podanych przez uzytkownika wartosci
a oraz n oblicza potege a^n. Liczba a jest liczba calkowita, natomiast
liczba n jest liczba calkowita nieujemna.
Obliczenia powinne byc wykonane w funkcji, która przyjmuje dwa argumenty i zwraca wynik.
Wywołanie funkcji obliczającej odpowiednią potęgę a^n umieść w funkcji main(),
zarówno liczba a, jak i n powinna zostać wprowadzona przez użytkownika z klawiatury.
Wynik wyświetl w funkcji main w stosownym formacie.
'''

def potega(a,n): # 2
    return a**n # 2 

def main():
    liczba = int(input("Podaj liczbę całkowitą - podstawę potęgowania: ")) # 2
    p = int(input("Podaj liczbę całkowitą - wykladnik potęgowania: ")) # 2

    wynik = potega(liczba,p) # 1

    print(liczba,"^",p,"=",wynik, sep='') # 1

main()

