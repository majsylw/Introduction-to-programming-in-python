"""
Napisz program który pozwoli na pobranie 2 liczb całkowitych
i wyświetli największą z  nich.

"""

def main():
    a = int(input("Podaj liczbę: "))
    b = int(input("Podaj liczbę: "))
    if a > b:
        print("Największą liczbą jest", a)
    else:
        print("Największą liczbą jest", b)

main()
