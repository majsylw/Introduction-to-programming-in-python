'''
Napisz program, w którym użytkownik podaje po kolei liczby całkowite
aż do momentu, gdy dwie kolejne liczby będą takie same.
Na koniec podaj liczbę wczytanych liczb. UWAGA Nie musisz sprawdzać
czy dane wprowadzane przez użytkownika są poprawne (tzn. czy są to
faktycznie liczby całkowite).
'''

def main():
    liczba = int(input("Podaj liczbę: "))
    i = 1
    kolejna = None
    while kolejna != liczba:
        kolejna = liczba
        liczba = int(input("Podaj kolejną liczbę: "))
        i += 1
    print("Liczba podanych liczb:", i)
main()
