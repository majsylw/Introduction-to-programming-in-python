"""
Wstep do programowania
Zaliczenie czastkowe 2
28.11.2019 grupa P11-57j
imie: Maksymilnian
nazwisko: Maksimus
indeks: 000000
"""

'''
Zadanie 3 ( 4pkt.)
Ponizszy program oblicza sumę dwoch liczb wymiernych (ulamkow zwyklych).
Prosi on kolejno o wprowadzenie licznika i mianownika dwoch ulamkow.
Dopuszczalnym jest wprowadzenie przez uzytkownika ulamkow niewlasciwych
(licznik jest wiekszy od mianownika), ale nie ma mozliwosci
wprowadzenia ułamkow mieszanych (liczba calkowita i ulamek).
Uzupelnij program o odpowiednie wywolanie funkcji dodawanie_ulamkow.
Pamiętaj, żeby nie dopuścić do dzielenia przez zero.
Wyswietl ostateczny wynik w zrozumialej postaci.

'''

def dodawanie_ulamkow(licznik1,mianownik1,licznik2,mianownik2):
    return licznik1*mianownik2+licznik2*mianownik1, mianownik1*mianownik2


def main():
    licznik1 = int(input("Podaj pierwszy licznik: "))
    mianownik1 = int(input("Podaj pierwszy mianownik: "))

    licznik2 = int(input("Podaj drugi licznik: "))
    mianownik2 = int(input("Podaj drugi mianownik: "))

    # od tego miejsca uzupelnij swoj kod
    l_wynik, m_wynik = dodawanie_ulamkow(licznik1,mianownik1,licznik2,mianownik2) # 1
    
    if mianownik1 != 0 and mianownik2 != 0: # 1
        print(licznik1,"/",mianownik1,' + ',licznik2,"/",mianownik2," = ",l_wynik,'/',m_wynik, sep="") # .5
    else: # 1
        print("Niepoprawne dzielenie przez 0!") # .5
main()
