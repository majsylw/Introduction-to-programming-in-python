'''
Napisz program, który wylicza średnią arytmetyczną ocen podawanych przez
użytkownika. Użytkownik powinien określić ile ocen chce podać.
'''
# wersja podstawowa przy uzyciu petli for
def main_for():
    liczba_ocen = int(input("Podaj liczbe ocen: "))
    suma = 0
    
    for i in range(liczba_ocen):
        ocena = float(input("Podaj ocene: "))
        suma += ocena
    srednia = suma/liczba_ocen
    print("Twoja srednia wyniesie: ", format(srednia,".2f"))

# wersja podstawowa przy uzyciu petli while
def main_while():
    liczba_ocen = int(input("Podaj liczbe ocen: "))
    krok = 0
    suma = 0
    while krok < liczba_ocen:
        ocena = float(input("Podaj ocene: "))
        krok += 1
        suma += ocena
    srednia = suma/liczba_ocen
    print("Twoja srednia wyniesie: ", format(srednia,".2f"))

        
# wersja rozszerzona: oceny należą do zbioru {2, 3, 3.5, 4, 4.5, 5, 5.5}    
def main2():
    liczba_ocen = int(input("Podaj liczbe ocen: "))
    krok = 0
    suma = 0
    while krok < liczba_ocen:
        ocena = float(input("Podaj ocene: "))
        if ocena == 2 or ocena == 3 or ocena == 3.5 or ocena == 4 or ocena == 4.5 or ocena == 5 or ocena == 5.5:
            krok += 1
            suma += ocena
        else:
            print("Podales zla ocene! Sprobuj jeszcze raz.")
    srednia = suma/liczba_ocen
    print("Twoja srednia wyniesie: ", format(srednia,".2f"))
    
main_for()
main_while()
main2()
