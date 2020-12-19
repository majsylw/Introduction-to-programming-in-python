'''
Napisz program, który pozwoli na sprawdzenie czy podany przez użytkownika
napis jest palindromem, tzn. czytany od przodu, jaki i od końca pozwala
na odczytanie tego samego wyrazu. Na potrzeby tego zadania możesz założyć,
że użytkownik zawsze wpisze pojedyncze słowo.

Przykładowe wywołania:

Podaj słowo: kajak
To słowo jest palindromem

Podaj słowo: ala
To słowo jest palindromem

Podaj słowo: hipopotam
To słowo nie jest palindromem.
'''

def main():
    slowo = input("Podaj jedno słowo: ")
    dlugosc = len(slowo) - 1
    for i in range(int(len(slowo) // 2)):
        if slowo[i] != slowo[dlugosc - i]:
            print("Podane słowo nie jest palindromem.")
            break
    else:
        print("Podane słowo jest palindromem.")
main()
