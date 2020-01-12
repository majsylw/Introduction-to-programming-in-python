'''
Napisz program, który oblicza wartość funkcji f(x) = a⋅x + b, dla podanych przez
użytkownika współczynników a i b oraz zmiennej x. Obliczoną wartość program
powinien wypisywać na ekran.
W programie wydziel funkcję, która pobiera trzy argumenty i wyświetla wynik.
Zastanów się, jaki jest związek między obliczaniem wartości funkcji f(x), a przeliczaniem
różnych skal temperatur (patrz zadanie 5 z listy 2).
'''

def funkcja_liniowa(a,b,x):
    y = a*x+b
    return y

def main():
    x = float(input("Podaj x: "))
    wspolczynnik_kierunkowy = float(input("Podaj wspolczynnik kierunkowy prostej: "))
    wyraz_wolny = float(input("Podaj wyraz wolny prostej: "))

    wynik = funkcja_liniowa(x=x, a=wspolczynnik_kierunkowy, b=wyraz_wolny)

    print(wspolczynnik_kierunkowy,"*",x,"+",wyraz_wolny,"=",wynik)

    # Dla konwersji roznych skal temperatur
    # Celsjusz -> Farenheit
    a = 9/5
    b = 32
    print(100,"st. Celsjusza to",funkcja_liniowa(a,b,100),"st. Farenheita")

main()
