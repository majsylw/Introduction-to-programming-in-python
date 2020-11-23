'''
Napisz program, który rozwiązuje równanie a⋅x + b = 0. Współczynniki równania
(a, b) powinny być podane przez użytkownika. Zwróć uwagę, że – dla pewnych
wartości współczynników – równanie nie będzie miało dokładnie jednego rozwiązania
(może być sprzeczne lub nieoznaczone). W swoim rozwiązaniu wyszczególnij:
- funkcję czy_rozwiązanie() która sprawdzi czy podane równanie ma jakiekolwiek
rozwiązanie i zwróci odpowiednią wartość logiczną;
- funkcję wartość_funkcji(), która przyjmuje jako argumenty współczynnik kierunkowy
a, współczynnik wolny b i wyznacza wartość równania, gdy ma ono dokładnie jedno
rozwiązanie, po czym zwraca je,
- funkcję main(), w której przeprowadzisz interakcję z uzytkownikiem - pobierzesz
od niego dane współczynnikach równania, a następnie sprawdzisz warunki jego
istnienia (czy mamy równanie sprzeczne, oznaczone czy nieoznaczone). Pamiętaj
aby w każdym przypadku wyświetlić stosowny komunikat oraz o wywołaniu funkcji
wartość_funkcji() gdy rówanie będzie miało dokładnie jedno rozwiązanie.
Rozwiązanie załącz w postaci pliku *.py.
'''

def wartość_funkcji(a, b):
    if czy_rozwiązanie(a)
        return -b/a
    else:
        return None

def czy_rozwiązanie(wsp_kierunkowy):
    if wsp_kierunkowy == 0:
        return True
    else:
        return False

def main_liniowa():
    a = float(input("Podaj współczynnik kierunkowy: "))
    b = float(input("Podaj wyraz wolny: "))
    if not czy_rozwiązanie(a):
        if b == 0:
            print("Równanie ma nieskończenie wiele rozwiązań.")
        else:
            print("Równanie jest sprzeczne.")
    else:
        wynik = wartość_funkcji(a, b)
        print(a,"⋅",wynik,format(b,"+.2f"), "= 0")
main_liniowa()

'''
lista 6 zadanie ostatnie
'''
def delta(a, b, c):
    return b**2 - 4 * a * c

def main_kwadratowa():
    a = float(input("Podaj współczynnik a: "))
    b = float(input("Podaj współczynnik b: "))
    c = float(input("Podaj współczynnik c: "))
    if a == 0:
        if b == 0:
            if c == 0:
                print("Równanie ma nieskończenie wiele rozwiązań.")
            else:
                print("Równanie jest sprzeczne.")
        else:
            wynik = wartość_funkcji(b, c)
            print(b, "⋅", format(wynik,".2f"), format(c,"+.2f"), "= 0")
    else:
        d = delta(a, b, c)
        if d < 0:
            print("Brak rozwiązań rzeczywistych.")
        elif d == 0:
            print("Dokładnie jedno rozwiązanie postaci",
                  -b / 2 / a)
        else:
            print("Dokładnie dwa rozwiązania postaci",
                  (-b + d**0.5) / 2 / a, "oraz", (-b - d**0.5) / 2 / a)
main_kwadratowa()                  
