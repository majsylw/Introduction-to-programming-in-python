"""
Wstep do programowania
Zaliczenie czastkowe 3
19.12.2019 grupa P11-57j
imie:
nazwisko:
indeks:
"""

'''
Zadanie 2 (9 pkt.)
Napisz program, ktory wykona się zadaną przez użytkownika liczbę razy.
W każdej iteracji pętli:
- pobierz od uzytkownika liczbe calkowita
– wyświetl informację czy liczba jest wielokrotnoscia 3
– wyświetl informację czy liczba jest wielkorotnoscia 4
– wyswietl „hurra” jeżeli liczba dzieli się zarówno przez 3 jak i 4
– wyswietl gwiazdke, jeśli żaden z powyższych warunkow nie jest spełniony.
'''

def main():
    ile = int(input("Podaj ile razy chcesz wykonac program: "))

    for i in range(ile):
        liczba = int(input("Podaj liczbe: "))
        if liczba%3==0 and liczba%4==0:
            print("Hurra! Liczba dzieli sie przez 3 i 4!")
        elif liczba%4 == 0:
            print("Liczba dzieli sie przez 4!")
        elif liczba%3==0:
            print("Liczba dzieli sie przez 3!")
        else:
            print("*")
main()
