'''
Napisz funkcję czy_podzielna_2(), które sprawdza czy podana jako argument
liczba całkowita jest podzielna przez 2.

Napisz funkcję czy_podzielna_3(), które sprawdza czy podana jako argument
liczba całkowita jest podzielna przez 3.

Następnie napisz funkcję czy_podzielna_6(), które sprawdza czy podana jako
argument liczba całkowita jest podzielna przez 6. W implementacji tej
funkcji wykorzystaj fakt, że liczba podzielna przez 6 musi być podzielna
przez 2 i podzielna przez 3. 

Następnie napisz prosty program, który demonstruje działanie funkcji
podzielna_6(). Program powinien prosić użytkownika o podanie liczby
całkowitej i wyświetlać komunikat o jej podzielności przez 6.
'''
def czy_podzielna_2(a):
    if a % 2 == 0:
        return True
    else:
        return False

def czy_podzielna_3(a):
    if a % 3 == 0:
        return True
    else:
        return False

def czy_podzielna_6(a):
    if czy_podzielna_2(a) and czy_podzielna_3(a):
        return True
    else:
        return False
def main():
    liczba = int(input("Podaj liczbę całkowitą: "))
    if czy_podzielna_6(liczba):
        print("Liczba", liczba, "jest podzielna przez 6.")
    else:
        print("Liczba", liczba, "nie jest podzielna przez 6.")
main()
