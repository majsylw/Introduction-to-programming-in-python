'''
Zadanie 6
Pozwol uzytkownikowi wprowadzic dowolną liczbe imion ciagiem 
(np. jako jeden string, rozdzielone przecinkiem). 
Nastepnie powitaj kazda osobe na liscie poprzez cykliczne wyswietlenie „Czesc <imie>!”.
Dodatkowo zlicz liczbę członków grupy (i podaj tę liczbę na koniec działania programu),
ale jeśli liczba członków grupy będzie większa od 3 - przerwij działanie pętli 
i wypisz komunikat o niedozwolonej liczbie osób.

Przykladowe wywolania programu:

Czesc, podaj imiona czlonkow grupy rozdzielone ,: Ada,Kinga,Michal,Bartek,Sławek
Czesc, Ada!
Czesc, Kinga!
Czesc, Michal!
Czesc, Bartek!
UWAGA! Twoja grupa liczy już 4 osoby - liczebność grupy musi być mniejsza od 3!

Czesc, podaj imiona czlonkow grupy rozdzielone ,: Ada,Kinga
Czesc, Ada!
Czesc, Kinga!
Twoja grupa liczy 2 osoby.

'''

def main():
    wiersz = input("Czesc, podaj imiona czlonkow grupy rozdzielone ,: ")
    licznik = 0
    print("Czesc, ",end="")
    for i in wiersz:
        if i == ",":
            licznik += 1
            if licznik < 4:
                print("!\nCzesc, ", end="")
        else: 
            print(i, end="")
        if licznik > 3:
            print("!\nUWAGA! Twoja grupa liczy już 4 osoby - liczebność grupy musi być mniejsza od 3!")
            break
    else:
        if licznik + 1 > 3:
            print("!\nUWAGA! Twoja grupa liczy już 4 osoby - liczebność grupy musi być mniejsza od 3!")
        else:
            print("!\nTwoja grupa liczy", licznik + 1 ,"osoby.")

main()

# Input -> 1
# petla -> 2
# warunek -> 2
# Komunikat czesc <imie> w jednej linii -> 2
# Zatrzymanie przy zliczeniu więcej niż 3 osób -> 1
# Wykrzyknik na koncu kazdego powitania -> 1
