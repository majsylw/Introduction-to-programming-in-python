'''
Napisz program, który będzie wyświetlał następujące informacje:
- Twoje imię i nazwisko
- Twój kierunek studiów
- Twój numer indeksu
Przed przystąpieniem do pisania programu zaprojektuj algorytm.
Każdy komunikat umieść w osobnej funkcji – łącznie program powinien składać się z 4
funkcji.

'''

def dane_osobowe():
    Imie = input("Podaj imie i nazwisko: ")
    #input("Podaj imie i nazwisko: ")
    print(Imie)
    
def nr_indeksu():
    indeks = input("podaj nr indeksu")
    print(indeks)

def kierunek():
    #kierunek = input("podaj kierunek studiow:")
    print(input("podaj kierunek studiow:"))
               
def main():

    dane_osobowe()
    nr_indeksu()
    kierunek()

main()
