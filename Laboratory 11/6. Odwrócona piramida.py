'''
Napisz program, który pozwoli na narysowanie odwróconej piramidy
z x (patrz rysunek poniżej) o wysokości zadanej przez użytkownika
(użytkownik wpisuje liczbę z klawiatury).

Przykładowe wywołanie:

Podaj wysokość piramidy: 3
xxxxx
 xxx
  x
'''

def main():
    znak = "x"
    n = int(input("Podaj wysokość piramidy: "))
    for i in range(n - 1, -1, -1):
        print(" " * (n - i - 1) + znak * ( 2 * i + 1))

main()
