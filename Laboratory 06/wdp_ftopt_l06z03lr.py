'''
Napisz program, który rozwiązuje równanie a⋅x + b = 0. Współczynniki równania (a, b)
powinny być podane przez użytkownika.
Zwróć uwagę, że – dla pewnych wartości współczynników – równanie nie będzie miało
dokładnie jednego rozwiązania (może być sprzeczne lub nieoznaczone).

'''

def miejsce_zerowe_funkcji_liniowej(a,b):
    x = -b/a
    return x

def main():
    wspolczynnik_kierunkowy = float(input("Podaj wspolczynnik kierunkowy prostej: "))
    wyraz_wolny = float(input("Podaj wyraz wolny prostej: "))

    if wspolczynnik_kierunkowy != 0:
        wynik = miejsce_zerowe_funkcji_liniowej(a=wspolczynnik_kierunkowy, b=wyraz_wolny)
        print(wspolczynnik_kierunkowy,"*",wynik,"+",wyraz_wolny,"=",0)
    else:
        if wyraz_wolny == 0:
            print("Rownanie ma nieskonczenie wiele rozwiazan: x =",wyraz_wolny)
        else:
            print("Rownanie nie ma rozwiazan: x =", wyraz_wolny)

main()
