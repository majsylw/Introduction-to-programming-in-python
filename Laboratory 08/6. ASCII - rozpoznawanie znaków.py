'''
Napisz program wyświetlający informacje o klawiszu 
wciśniętym na klawiaturze – jego kategorię.
Program przyjmuje odpowiednie wyrażenie i wypisuje informacje o nim,
a następnie kończy działanie. Program powinien rozpoznawać znaki:
- Małe litery (kody ASCII od a do z: 97 - 122)
- Duże litery (kody ASCII od A do Z: 65 - 90)
- Spacja
- Operatory porównania dla ostrej nierówności: >, <
W przypadku gdy nie zostanie podana żadna z powyższych opcj
program ma wypisać informację "Nierozpoznany znak."
W swoim rozwiązaniu wyszczególnij:
- funkcję czy_pojedynczy_znak() która będzie pobierała jako argument 
napis wpisany przez użytkownika oraz sprawdzała jego długość (funkcja len()). 
Jeśli napis będzie miał więcej niż lub mniej niż jeden znak to zwróci fałsz, 
gdy dokładnie jeden znak - prawdę,
- funkcję main() w której poprowadzisz interakcję z użytkownikiem - wczytasz 
potrzebne dane, i sprawdzisz, czy podany przez użytkownika napis ma 
odpowiednią liczbę znaków (korzystając ze zdefiniowanej przez 
siebie funkcji). Jeśli tak będzie to program powinien podać 
interpretację uzyskanego wyniku, tzn. wydrukować na ekran komunikat 
na temat tego, do której z czterech kategorii (tzn. małe litery, 
wielkie litery, operatory ostrych nierówności, spacja) należy 
wpisane wyrażenie. Zadbaj o to, aby także gdy nie zostanie 
podana żadna ze znanych opcji na ekranie konsoli 
pojawił się adekwatny komunikat.
Swoje rozwiązanie załącz w pliku *.py.
'''

def informacja_o_znaku(znak):
    print("Nacisnieto ", znak, ", kod znaku to: ", str(ord(znak)), sep="")

def czy_pojedynczy_znak(napis):
    if len(napis) == 1:
        return True
    else:
        return False

def main():
    napis = input("Podaj znaki: ")
    if czy_pojedynczy_znak(napis):
        if ord(napis) >= 97 and ord(napis) <= 122:
            print("Znak jest małą literą.")
            informacja_o_znaku(napis)
        elif ord(napis) >= 65 and ord(napis) <= 90:
            print("Znak jest wielką literą.")
            informacja_o_znaku(napis)
        elif napis == " ":
            print("Znak jest spacją.")
            informacja_o_znaku(napis)
        elif napis == ">" or napis == "<":
            print("Znak jest operatorem relacji.")
            informacja_o_znaku(napis)
        else:
            print("Nierozpoznany znak!")
    '''
    # Pierwotna wersja zadania obejmowała wszystkie operatory relacji
    elif len(napis) == 2:
        if (napis[0] == '=' or
            napis[0] == '!' or
            napis[0] == '<' or
            napis[0] == '>') and napis[1] == '=':
            print("Wyrażenie jest operatorem relacji.")
            informacja_o_znaku(napis[0])
            informacja_o_znaku(napis[1])
        else:
            print("Nierozpoznane wyrażenie!")
    '''
    else:
        print("Nierozpoznane wyrażenie!")

main()
