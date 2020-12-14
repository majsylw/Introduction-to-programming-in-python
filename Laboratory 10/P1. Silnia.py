'''
Napisz program, który prosi użytkownika o podanie dodatniej liczby całkowitej,
a następnie wyświetla silnię podanej liczby.
'''
def silnia(n):
    if n >= 0:
        iloczyn = 1
        for i in range(2,n+1):
            iloczyn *= i
        return iloczyn

def main():
    liczba = int(input("Podaj liczbę całkowitą: "))
    if liczba >= 0:
        wynik = silnia(liczba)
        print(liczba, "! = ", wynik, sep="")
    else:
        print("Podano złą liczbę.")

main()