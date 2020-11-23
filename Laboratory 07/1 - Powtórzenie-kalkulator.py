'''
Napisz prosty kalkulator, tzn. funkcję calc(a, b, c), która w wyniku zwraca:

-sumę liczb a, b, jeśli c =”+”;
-różnicę liczb a, b, jeśli c =”-”;
-iloczyn liczb a, b, jeśli c =”*”;
-iloraz liczb a, b, jeśli c =”/”.

Przetestuj jej działanie na pobranych od użytkownika 2 liczbach całkowitych
i znaku definiującego. W swoim rozwiązaniu wyszczególnij:
- funkcję czy_poprawny_znak(), która jako argument przyjmie znak wpisany
przez użytkownika i sprawdzi czy kalkulatro może wykonać dane działanie,
w odpowiedzi powinna zwrócić wartość logiczną;
- funkcję calc(), która przyjmuje jako argumenty dwie liczby i znak, na tej
podstawie dokonuje odpowiednich obliczeń, na koniec zwraca uzyskany wynik
- funkcję main(), w której przeprowadzisz interakcję z uzytkownikiem - pobierzesz
od niego dane odwóch liczbach całkowitych oraz znaku i sprawdzisz ich poprawność,
a następnie za pomocą funkcji calc() wykonasz odpowiednią operację
na wprowadzonch danych, na koniec wypisz na ekranie komunikat o wyniku.
Rozwiązanie załącz w postaci pliku *.py.
'''

def calc(a, b, c):
    if c == "+":
        return a + b
    if c == "-":
        return a - b
    if c == "*":
        return a * b
    if c == "/":
        return a // b
    return None
def czy_poprawny_znak(c):
    if c == "+" or c == "-" or c == "*" or c == "/":
        return True
    return False
def main():
    l1 = int(input('Podaj liczbę: '))
    l2 = int(input('Podaj liczbę: '))
    znak = input('Podaj znak działania: ')
    if czy_poprawny_znak(znak):
        wynik = calc(l1, l2, znak)
        print(l1, znak, l2, "=", wynik)
    else:
        print("Nie ma takiej operacji!")
main()
                  
