'''
Liczba pierwsza to taka liczba naturalna, która jest większa od 1 i dzieli się tylko 
przez 1 i sama siebie, czyli posiada jedynie dwa dzielniki. Napisz program, 
który sprawdzi czy podana przez użytkownika liczba całkowita jest liczbą pierwszą. 
W obu przypadkach wypisz na ekran stosowny komunikat. Pamiętaj aby sprawdzić czy użytkownik 
nie wprowadził liczby ujemnej!
'''
def main():
    liczba = int(input("Podaj liczbę naturalną: "))
    for i in range(2, liczba*):
        if liczba%i == 0:
            break
    else:
        print(liczba, "jest liczbą pierwszą")
    if i != liczba-1:
        print(liczba, "nie jest liczbą pierwszą")
main()
