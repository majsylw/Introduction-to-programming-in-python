"""
Wstep do programowania
Kolokwium termin 0
9.01.2019 grupa P11-57j
imie:
nazwisko:
indeks:
"""

'''
Zadanie 1 (15 pkt.)
Aby zrelaksować się w trakcie kolokwium postanawiasz
napisać grę "papier, kamień, nożyce" i zagrać z komputerem.
Reguły gry:
- papier wygrywa z kamieniem, kamień wygrywa z nożycami
  a nożyce wygrywają z papierem,
- papier z papierem, kamień z kamieniem i nożyce z nożycami remisują.

Punktacja:
- komunikacja z użytkownikem i pobranie wartości zmiennych odpowiednich typów (4 pkt.),
- sprawdzenie, czy użytkownik podał poprawną wartość (2 pkt),
- wylosowanie wyboru komputera i przypisanie go do zmiennej (2 pkt.),
- porównanie wyboru komputera z wyborem użytkownika i ustalenie
  zwycięstwa jednej ze stron lub remisu (7 pkt.).


Program będzie oceniany tylko w przypadku,
gdy będzie można go uruchomić!
----------------------------------------------------
Przykładowe wyniki uruchomienia programu:

Zagrajmy w "papier, kamien, nozyce"!
Zaczyna uzytkownik, wybierajac:
1 - papier
2 - kamien
3 - nozyce
Podaj swoj wybor: 3
Uzytkownik wybral papier.
Komputer wylosowal kamien.
Uzytkownik wygrywa.

Zagrajmy w "papier, kamien, nozyce"!
Zaczyna uzytkownik, wybierajac:
1 - papier
2 - kamien
3 - nozyce
Podaj swoj wybor: 3
Uzytkownik wybral nozyce.
Komputer wylosowal kamien.
Komputer wygrywa.

Zagrajmy w "papier, kamien, nozyce"!
Zaczyna uzytkownik, wybierajac:
1 - papier
2 - kamien
3 - nozyce
Podaj swoj wybor: 3
Uzytkownik wybral nozyce.
Komputer wylosowal nozyce.
Remis.

Zagrajmy w "papier, kamien, nozyce"!
Zaczyna uzytkownik, wybierajac:
1 - papier
2 - kamien
3 - nozyce
Podaj swoj wybor: 5
Wybrales nieprawidowo. Koniec gry.

----------------------------------------------------
'''
import random

def main():
    print('Zagrajmy w "papier, kamien, nozyce"!')
    print('Zaczyna uzytkownik, wybierajac:')
    print('\t1 - papier')
    print('\t2 - kamien')
    print('\t3 - nozyce')

    choice = int(input("Podaj swoj wybor: "))
    if choice == 1 or choice == 2 or choice == 3:
        computer = random.randint(1,3)
        if choice == 1:
            print("Uzytkownik wybral papier.")
            if computer == 1:
                print("Komputer wybral papier.")
                print("Remis")
            if computer == 2:
                print("Komputer wybral kamien.")
                print("Uzytkownik wygrywa")
            if computer == 3:
                print("Komputer wybral nozyce.")
                print("Komputer wygrywa")
        if choice == 2:
            print("Uzytkownik wybral kamien.")
            if computer == 1:
                print("Komputer wybral papier.")
                print("Komputer wygrywa")
            if computer == 2:
                print("Komputer wybral kamien.")
                print("Remis")
            if computer == 3:
                print("Komputer wybral nozyce.")
                print("Uzytkownik wygrywa")
        if choice == 3:
            print("Uzytkownik wybral nozyce.")
            if computer == 1:
                print("Komputer wybral papier.")
                print("Uzytkownik wygrywa")
            if computer == 2:
                print("Komputer wybral kamien.")
                print("Komputer wygrywa")
            if computer == 3:
                print("Komputer wybral nozyce.")
                print("Remis")
    else:
        print("Wybrales nieprawidowo. Koniec gry.")

main()
