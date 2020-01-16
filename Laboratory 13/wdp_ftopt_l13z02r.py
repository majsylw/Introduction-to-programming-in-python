"""
Wstep do programowania
Kolokwium termin 0
16.01.2019 grupa P11-57j
imie:
nazwisko:
indeks:
"""

'''
Zadanie 2 (15 pkt.)
Napisz program, który oblicza wartości funkcji sin(x)/x
dla argumentów z przedziału od -1 do 1.   
Liczba punktów powinna być podawana przez użytkownika z klawiatury.
Jeśli użytkownik poda liczbę niedodatnią poproś o podanie
liczby kolejny raz (aż do momentu uzyskania prawidłowej liczby).
Wynik działania sin(x)/x dla x = 0 zastąp wartością
            lim sin(x)/x dla x -> 0
Wyniki wypisz w postaci tabeli o dwóch kolumnach
z liczbami zaokrąglonymi do 2 miejsc po przecinku.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Przykładowy efekt działania programu.

Podaj liczbe punktow: 10
x 		 sin(x)/x
--------------------------
-1.00 		 0.84
-0.80 		 0.90
-0.60 		 0.94
-0.40 		 0.97
-0.20 		 0.99
0.00 		 1
0.20 		 0.99
0.40 		 0.97
0.60 		 0.94
0.80 		 0.90
'''
from math import sin

def main():
    n = int(input("Podaj liczbe punktow: ")) # 1

    while n <= 0: # 2
        n = int(input("Liczba n musi być dodatnia! Podaj liczbe punktow: ")) # 1

    print('x',"\t\t",'sin(x)/x')
    print('--------------------------')
    krok = 2/n # 1
    for i in range(n): # 2
        if (-1+i*krok) != 0: # 2
            print(format(-1+i*krok,".2f"),"\t\t",format(sin(-1+i*krok)/(-1+i*krok),".2f")) # 4
        else: # 1
            print(format(-1+i*krok,".2f"),"\t\t",1) # 1
        

main()

