'''
Załóżmy, że podatek dochodowy wyliczany jest według następujących stawek:
-Przychody do 4000 zł nie są opodatkowane. 
-Przychody pomiędzy 4000 a 90000 zł są objęte stawką 20% podatku.
-Przychody powyżej 90000 zł objęte są stawką 30% podatku. 
Napisz program, który dla podanej (w zł) kwoty obliczy należny podatek dochodowy.
W swoim rozwiązaniu wyszczególnij:
-funkcję czy_poprawny(), która jako argument przyjmuje wysokość dochodu i
zwraca prawdę lub fałsz w zależności od tego czy odchód nie jest ujemny;
funkcję wylicz_podatek(), która przyjmuje jako argumenty wysokość dochodu oraz
stawkę procentową podatku, a zwraca wyskość podatku
-funkcję main(), w której przeprowadzisz interakcję z uzytkownikiem - pobierzesz
od niego dane o wysokości podatku i sprawdzisz jego poprawność, a następnie
gdy wszystko będzie ok to za pomocą odpowiednich instrukcji
warunkowych wyznaczysz stawkę podatku, na koniec wylicz podatek dochodowy
korzystając ze swojej funkcji wylicz_podatek() i wypisz na ekranie komunikat
ile on wynosi. Pamiętaj aby wypisać komunikat o niepoprawnych danych!
Rozwiązanie załącz w postaci pliku *.py.
'''

def wylicz_podatek(dochod, stawka):
    return dochod * stawka
def czy_poprawny(c):
    if c >= 0:
        return True
    return False
def main():
    d = float(input('Podaj swój dochód: '))
    if czy_poprawny(d):
        if d <= 4000:
            p = wylicz_podatek(d, 0)
        elif d > 4000 and d <= 90000:
            p = wylicz_podatek(d, 0.2)
        else:
            p = wylicz_podatek(d, 0.3)
        print("Podatek od dochodu", d,"zł wyniesie", p, "zł.")
    else:
        print("Dochód nie może być ujemny!")
main()
                  
