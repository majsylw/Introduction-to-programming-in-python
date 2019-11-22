# Funkcja calc pobiera 2 liczby calkowite i znak dzialania
# w zaleznosci od ktorego wykona odpowiednie operacje
# Funkcja zwraca wynik danej operacji
# w przypadku, gdy uzytkownik prowadzi znak spoza ustalonej listy znakow
# funkcja zwroci False
def calc(a,b,c):
    if c == '*':
        return a*b
    elif c == '/':
        # Uwaga na dzielenie przez 0!
        if b != 0:
            return a/b
        else:
            None
    elif c == '+':
        return a+b
    elif c == '-':
        return a-b
    else:
        return False

def main():
    liczba1 = int(input("Wpisz pierwsza liczbe calkowita: "))
    liczba2 = int(input("Wpisz druga liczbe calkowita: "))
    znak = input("Jakie dzialanie chcesz wykonac? Wpisz znak +, -, / lub *: ")

    # Uwaga na bezposrednie porownywanie
    # w przypadku zastosowania != wyliczone 0 takze uznano by za nieprawde
    # np. 4-4=0 (program zadzialalby niepoprawnie)
    if calc(liczba1,liczba2,znak)is not False:
        print(liczba1,znak,liczba2,"=",calc(liczba1,liczba2,znak))
    else:
        print("Wpisales niepoprawny znak dzialania!")

main()
