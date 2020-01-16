"""
Wstep do programowania
Kolokwium termin 0
9.01.2019 grupa P11-57j
imie:
nazwisko:
indeks:
"""

'''
Zadanie 1 (15 pkt.)
Napisz program, ktory:
- pobiera od uzytkownika numer pesel,
- sprawdza czy podany pesel jest poprawny, tzn.
  sprawdź czy poniższe wyrażenie jest podzielne przez 10:
  PESEL[0] + 3*PESEL[1] + 7*PESEL[2] + 9*PESEL[3] + PESEL[4] + 3*PESEL[5] + 7*PESEL[6] + 9*PESEL[7] + PESEL[8] + 3*PESEL[9] + PESEL[10],
  gdzie PESEL[i] - to kolejne cyfry numeru pesel licząc od 0 do 10,
- jesli tak to sprawdza czy osoba urodziła się w latach 1997 do 1999,
  czyli czy dwa pierwsze znaki reprezentują odpowiedni rok,
  np. dla roku 1997 będzie to '97', dla 1999 będzie to '99',
- jesli tak, to sprawdza czy jest ona mężczyzną,
  czyli czy przedostatnia cyfra jest nieparzysta.
W sytuacji, w ktorej jeden z warunkow nie jest spelniony
program powinien wyswietlic odpowiednia informacje.

Szczegolowe wymogi dotyczace implementacji programu:
- pobierz od użtkownika zmienną odpowiedniego typu przechowujacą
  numer pesel (2 pkt)
- sprawdz kolejno odpowiednie warunki (4 pkt)
- jesli pesel jest niepoprawny, wyswietl odpowiednia informacje
  (1 pkt)
- jesli numer pesel jest poprawny, to sprawdz czy osoba urodziła się w latach 1997 do 1999
  (3 pkt)
- jesli osoba urodziła się w latach 1997-1999, sprawdz czy jest ona mężczyzną (3 pkt)
- jesli tak nie jest, to wyswietl odpowiednia informacje (1 pkt)
- zadbaj o to, aby program dokonywał odpowiednich operacji (sprawdzeń)
  tylko dla poprawnych danych i nie powielal tych samych komunikatow w roznych
  przypadkach (1 pkt)

Program bedzie oceniany tylko w przypadku,
gdy bedzie mozna go uruchomic!
----------------------------------------------------
Przykladowe wyniki uruchomienia programu:

Podaj numer pesel: 99070544743

Numer PESEL jest poprawny.
Osoba urodzila sie w latach 1997-1999!
Ten osobnik jest kobieta.
----------------------------------------------------
'''

def main():
    PESEL = input("Podaj swoj numer PESEL: ") # 2

    if not (int(PESEL[0]) + 3*int(PESEL[1]) + 7*int(PESEL[2]) + 9*int(PESEL[3]) + int(PESEL[4])+ 3*int(PESEL[5]) + 7*int(PESEL[6]) + 9*int(PESEL[7]) + int(PESEL[8]) + 3*int(PESEL[9]) + int(PESEL[10]))%10: # 2
        print("Numer PESEL jest poprawny!") # 1
        if PESEL[0]=='9' and (PESEL[1]=='7' or PESEL[1]=='8' or PESEL[1]=='9'): # 2
            print("Osoba urodzila sie w latach 1997-1999!") # 1
            if int(PESEL[9])%2:
                print("Ten osobnik jest mezczyzna!") # 1
            else: # 1
                print("Ten osobnik jest kobieta!") # 1
        else: # 1
            print("Osoba nie urodzila sie w latach 1997-1999!") # 1
    else: # 1
        print("Numer PESEL nie jest poprawny!") # 1
main()
