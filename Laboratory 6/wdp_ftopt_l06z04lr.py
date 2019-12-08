'''
Napisz program, który prosi użytkownika o podanie liczby punktów z kolokwium oraz
uzyskanych w trakcie semestru. Na tej podstawie wyświetla informacje o uzyskanej
ocenie zgodnie z zasadami zaliczenia kursu.
Algorytm przeliczania punktów na oceny zamknij w osobnej funkcji.

'''

def jaka_ocena(punkty):
    if punkty < 50:
        return 2.0
    elif punkty < 60:
        return 3.0
    elif punkty < 70:
        return 3.5
    elif punkty < 80:
        return 4.0
    elif punkty < 90:
        return 4.5
    elif punkty < 100:
        return 5.0
    else:
        return 5.5

def main():
    p = float(input("Podaj liczbe punktow: "))
    print("Twoja ocena to: ", jaka_ocena(p))

main()
