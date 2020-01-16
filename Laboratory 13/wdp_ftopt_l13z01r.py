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
Napisz program, ktory realizuje "slynny" schemat,
wedlug ktorego kazdy problem mozna rozwiazac przy
uzyciu tasmy klejacej albo preparatu WD40.

Program powinien zadan pytanie „Czy to się rusza?”
a uzytkownik powinien udzielac odpowiedzi,
- jesli "to" (czyli przedmiot problemu) sie rusza
  program powinien zadac pytanie czy to powinno sie
  ruszac,
- jesli powinno, to problem jest rozwiazany,
- jesli nie powinno to trzeba uzyc tasmy i problem
  rozwiazany.

- jesli "to" sie nie rusza program powiniene zadac
  pytanie czy powinno,
- jesli nie powinno, to problem jest rozwiazany,
- jesli powinno to trzeba uzyc WD40 i problem
  rozwiazany.

Szczegolowe wymogi dotyczace implementacji programu:
- zainicjalizuj potrzebne zmienne odpowiedniego typu (1 pkt)
- poprawnie zaprogramuj interakcje z uzytkownikiem - daj
  mu mozliwosc wyboru odpowiedzi (4 pkt)
- skonstruuj odpowiedni warunek sprawdzajacy odpowiedz
  i kierujacy dalsza czescia programu (3 pkt) 
- przypisz instrukcji else odpowiednie dzialanie (1 pkt)
- zaprogramuj kolejna interakcje z uzytkownikiem wewnatrz
  warunku (2 pkt)
- dla kazdego mozliwego wyniku wypisz odpowiedni komunikat
  (4 pkt)

Program bedzie oceniany tylko w przypadku,
gdy bedzie mozna go uruchomic!
----------------------------------------------------
Przykladowe wyniki uruchomienia programu:

Czy to sie rusza? (T/N) T
A powinno? (T/N) n
Uzyj tasmy!
----------------------------------------------------
'''

def main():
    odpowiedz = input("Czy to sie rusza? (T/N) ") #2

    if odpowiedz=="T" or odpowiedz=="t": # 2
        odpowiedz = input("A powinno? (T/N) ") #1
        if odpowiedz=="T" or odpowiedz=="t": # 1
            print("Problem rozwiazany!") # 1
        else: # 1
            print("Uzyj tasmy!") # 1
    else: # 1
        odpowiedz = input("A powinno? (T/N) ")#1
        if odpowiedz =="T" or odpowiedz=="t": # 1
            print("Uzyj WD40!") # 1
        else: # 1
            print("Problem rozwiazany!") # 1

main()











    

