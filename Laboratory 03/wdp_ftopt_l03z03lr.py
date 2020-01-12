'''
Napisz program, który prosi użytkownika o podanie dwóch liczb całkowitych.
Następnie wyświetla na ekranie wyniki ich dodawania, odejmowania, mnożenia,
dzielenia, dzielenia całkowitego, reszty z dzielenia, potęgowania.
'''

def dodawanie(liczba1,liczba2):
    print("suma:", liczba1 + liczba2)
    
def odejmowanie (liczba_1, liczba_2):
    wynik = liczba_1 - liczba_2
    print ("roznic:",wynik)
def mnozenie (liczba1, liczba2):
    wynik= liczba1*liczba2
    print ("iloczyn:",wynik)

def dziel_cal(liczba1,liczba2):
    wynik = liczba1//liczba2
    print(wynik)

    
def dziel_ulam(liczba1,liczba2):
    wynik = liczba1/liczba2
    print(wynik)


def dziel_mod(liczba1,liczba2):
    wynik = liczba1%liczba2
    print(wynik)

def potega(liczba1,liczba2):
    wynik = liczba1**liczba2
    print(wynik)
def main():
    liczba_calkowita = int(input("podaj liczbe calkowita"))
    liczba_calkowita2 = int(input("podaj druga liczbe calkowita"))
    #print(type(liczba_calkowita))
    dodawanie(liczba_calkowita, liczba_calkowita2)
    odejmowanie(liczba_calkowita, liczba_calkowita2)
    mnozenie(liczba_calkowita, liczba_calkowita2)
    dziel_cal(liczba_calkowita, liczba_calkowita2)
    dziel_ulam(liczba_calkowita, liczba_calkowita2)
    dziel_mod(liczba_calkowita, liczba_calkowita2)
    potega(liczba_calkowita, liczba_calkowita2)
    
main()   
