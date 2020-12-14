'''
Napisz program, który dla dodatniej liczby całkowitej n, podanej przez użytkownika,
obliczy ile razy w jej zapisie wystąpiła jej maksymalna cyfra.
Przykładowo dla liczby 318338 program powinien podać wartość 2.
'''

def main():
    liczba = input("Podaj liczbę całkowitą: ")
    maksimum = 0
    licznik = 0
    for i in liczba:
        if int(i) > maksimum:
            maksimum = int(i)
            licznik = 0
        if int(i) == maksimum:
            licznik += 1
    
    print("Maksymalna cyfra", maksimum,"w liczbie", liczba, "wystąpi", licznik, "razy.")
main()