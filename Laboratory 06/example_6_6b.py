"""
Napisz program który pozwoli na pobranie 3 liczb całkowitych
i wyświetli największą z  nich.

"""

def najwieksza_vol1(a, b, c):
    if a > b and a > c:
        print("Największą liczbą jest", a)
        return a
    if b > a and b > c:
        print("Największą liczbą jest", b)
        return b
    else:
        print("Największą liczbą jest", c)
        return c

def najwieksza_vol2(a, b, c):
    najwieksza = a
    if b > najwieksza:
        najwieksza = b
    if c > najwieksza:
        najwieksza = c
    print("Największą liczbą jest", najwieksza)
    return najwieksza

def main():
    a = int(input("Podaj liczbę: "))
    b = int(input("Podaj liczbę: "))
    c = int(input("Podaj liczbę: "))

    najwieksza1 = najwieksza_vol1(a, b, c)
    najwieksza2 = najwieksza_vol2(a, b, c)
    if najwieksza1 != najwieksza2:
        print("Coś jest nie tak!")

main()
