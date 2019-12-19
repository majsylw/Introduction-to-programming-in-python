"""
Wstep do programowania
Zaliczenie czastkowe 3
19.12.2019 grupa P11-57j
imie:
nazwisko:
indeks:
"""

'''
Zadanie 1 (9 pkt.)
Pozwol uzytkownikowi wprowadzic dowolna liczbe imion ciagiem 
(np. jako jeden string, rozdzielone przecinkiem lub białym znakiem). 
Nastepnie pozdrów każdą osobę na liscie poprzez cykliczne wyswietlenie „Wesolych swiat, <imie>!”.

Przykladowe wywolanie programu:
Czesc, podaj imiona czlonkow grupy: Ada,Kinga,Michal,Bartek
Wesolych swiat, Ada!
Wesolych swiat, Kinga!
Wesolych swiat, Michal!
Wesolych swiat, Bartek!
'''
def main():
    imiona = input("Czesc, podaj imiona czlonkow grupy: ")
    #imiona = 'Ada,Kinga,Michal,Bartek'
    print("Wesolych swiat, ", end="")
    for i in imiona:
        if i != ',':
            print(i, end='')
        else:
            print("!\nWesolych swiat, ", end='')
    print("!")
main()

