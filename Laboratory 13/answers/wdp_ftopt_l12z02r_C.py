"""
Wstep do programowania
Kolokwium termin 0
9.01.2019 grupa P11-57j
imie:
nazwisko:
indeks:
"""
'''
Zadanie 2 (15 pkt.)
   Napisz program, który oblicza wartości funkcji 1/x
   dla przedziału od -1 do 1.   
   Liczba punktów powinna być podawana przez użytkownika z klawiatury.
   Jeśli użytkownik poda liczbę niedodatnia poproś o podanie
   liczby kolejny raz (aż do momentu uzyskania prawidłowej liczby).

   Wynik działania 1/x dla x = 0 zastąp slowem "NaN".

   Wyniki wypisz w postaci tabeli o dwóch kolumnach z liczbami zaokrąglonymi do 2 miejsc po przecinku.

   x        1/x
'''

def main():
    n = int(input("Podaj liczbe punktow: ")) # 1

    while n <= 0: # 2
        n = int(input("Liczba n musi być dodatnia! Podaj liczbe punktow: ")) # 1

    print('x\t\t1/x')
    krok = 2/(n-1) # 1
    for i in range(n): # 2
        if (-1+i*krok) != 0: # 2
            print(format(-1+i*krok,".2f"),"\t\t",format(1/(-1+i*krok),".2f")) # 4
        else: # 1
            print(format(-1+i*krok,".2f"),"\t\tNaN") # 1
        

main()

