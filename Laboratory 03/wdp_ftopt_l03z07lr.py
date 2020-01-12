'''
Napisz program, który oblicza wartość funkcji f(x) = a⋅x2 + b⋅x + c, dla podanych przez
użytkownika współczynników a, b i c oraz zmiennej x. Obliczoną wartość program
powinien wypisywać na ekran.
Zastanów się, w jaki sposób obliczać wartość funkcji, aby zminimalizować liczbę
wykonywanych działań.

'''

def trojmian(a,b,c,x):
    return a*x*x+b*x+c # 3 mnozenia
# dla mniejszej liczby mnozen
# https://pl.wikipedia.org/wiki/Schemat_Hornera
def trojmian_schemat_Hornera(a,b,c,x):
    return x*(x*a+b)+c # 2 mnozenia

def main():
    x = float(input("Podaj x: "))
    a = float(input("Podaj wspolczynnik a: "))
    b = float(input("Podaj wspolczynnik b: "))
    wyraz_wolny = float(input("Podaj wyraz wolny: "))

    wynik = trojmian(x=x, a=a, c=wyraz_wolny, b=b)

    print(a, " * ", x, "^2 + ", b, " * ", x, " + ", wyraz_wolny," = ",wynik,sep="")

main()
