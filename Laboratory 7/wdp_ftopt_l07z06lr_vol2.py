# Napisz program, ktory pobiera od uzytkownika pseudonimy 4 osob,
# a nastepnie wyewietla je w porzadku alfabetycznym.

# Na ile sposobow mozemy uszeregowac 4 osoby?
# odpowiedz na 4! = 24 -> czyli mamy 24 mozliwosci ustawien pseudonimow (kazdy print to inne ustawienie)

# Wersja 2 rozwiazania tego zadania
def main():
    p1 = input("Podaj pierwszy pseudonim: ")
    p2 = input("Podaj drugi pseudonim: ")
    p3 = input("Podaj trzeci pseudonim: ")
    p4 = input("Podaj czwarty pseudonim: ")

    print(sorted([p1,p2,p3,p4])) # soryujemy i wyswietlamy od razu

    # mozna tez tak
    # tworzymy liste pseudonimow w dowolnej koejnosci
    lista_pseudonimow = [p1,p2,p3,p4]
    # sortujemy liste
    lista_pseudonimow.sort()
    # wyswietlamy liste - zostala wczesniej posortowana za pomoca funkcji
    print(lista_pseudonimow)

main()
