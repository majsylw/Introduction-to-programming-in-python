'''
Napisz funkcje, która przyjmuje trzy zmienne logiczne x, y i z
(podane przez użytkownika) Jeżeli tylko jedna lub trzy ze zmiennych
ma wartość TRUE, to wyświetlij komunikat "Nieparzysta liczba".
Natomiast jeżeli dwie zmienne mają wartość TRUE, to wyświetlij
komunikat "Parzysta liczba".
'''

def sprawdz(x, y, z):
    if (((y == x == False  or
          x == z == False  or
          z == y == False) or
        x == y == z == True) and
        not (x == y == z == False)):
        print("Nieparzysta liczba")
    elif (y == x == True or
          x == z == True or
          z == y == True):
        print("Liczba parzysta")

def main():
    x = bool(int(input("Podaj wartość logiczną x: ")))
    y = bool(int(input("Podaj wartość logiczną y: ")))
    z = bool(int(input("Podaj wartość logiczną z: ")))

    sprawdz(x, y, z)

main()
