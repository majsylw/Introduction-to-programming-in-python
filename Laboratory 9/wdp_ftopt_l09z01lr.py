'''
Napisz program, który tworzy tabelę zestawiającą temperatury w stopniach Celsjusza
(od 0 do 40 co 2) i ich odpowiedniki w stopniach Fahrenheita.
'''
# wersja podstawowa z formatowaniem napisu
def drukuj_tabele():
    print('Temp. [deg C] \t Temp. [deg F]')
    # tworzymy liste od 0 do 40 co 2 stopnie
    for C in range(0,40+1,2):
        F = 32 + 9/5 * C
        print(format(str(C),'13s'),"\t",format(F,".2f"))
        
# wersja rozszerzona z podaniem temperatury poczatkowej, koncowej i kroku
def drukuj_tabele2(T0,Tk,krok):
    print('Temp. [deg C] \t Temp. [deg F]')
    # tworzymy liste od 0 do 40 co 2 stopnie
    for C in range(T0,Tk+1,krok):
        F = 32 + 9/5 * C
        print(format(str(C),'13s'),"\t",format(F,".2f"))
        
def main():
    # wersja podstawowa
    drukuj_tabele()
    # wersja rozszerzona
    drukuj_tabele2(5,100,5)
    

main()
