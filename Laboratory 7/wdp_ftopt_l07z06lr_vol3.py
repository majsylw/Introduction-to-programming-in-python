# Napisz program, ktory pobiera od uzytkownika pseudonimy 4 osob,
# a nastepnie wyewietla je w porzadku alfabetycznym.

# Na ile sposobow mozemy uszeregowac 4 osoby?
# odpowiedz na 4! = 24 -> czyli mamy 24 mozliwosci ustawien pseudonimow
# Wersja 3 rozwiazania tego zadania - przy wykorzystaniu funkcji min() i max()
def main():
    p1 = input("Podaj pierwszy pseudonim: ")
    p2 = input("Podaj drugi pseudonim: ")
    p3 = input("Podaj trzeci pseudonim: ")
    p4 = input("Podaj czwarty pseudonim: ")

    # szukamy minimum, maksimum posrod 4 napisow
    pierwszy = min(p1,p2,p3,p4)
    czwarty = max(p1,p2,p3,p4)

    # szukamy minimum, maksimum posrod 3 napisow
    if pierwszy == p4:
        drugi = min(p1,p2,p3)
    elif pierwszy == p1:
        drugi = min(p4,p2,p3)
    elif pierwszy == p2:
        drugi = min(p1,p4,p3)
    elif pierwszy == p3:
        drugi = min(p1,p2,p4)

    if czwarty == p4:
        trzeci = max(p1,p2,p3)
    elif czwarty == p1:
        trzeci = max(p4,p2,p3)
    elif czwarty == p2:
        trzeci = max(p1,p4,p3)
    elif czwarty == p3:
        trzeci = max(p1,p2,p4)

    print(pierwszy, drugi, trzeci, czwarty)

main()
