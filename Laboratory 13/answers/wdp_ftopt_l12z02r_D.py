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
Napisz program, który poprosi użytkownika o podanie dodatniej liczby naturalnej n.
Nastepnie wypisze na ekranie kolejne n wyrazów ciagu Fibonacciego.
Ciąg Fibonacciego to taki ciąg, którego dwa pierwsze wyrazy są równe 0 i 1. 
Każdy nastepny wyraz ciągu to suma dwóch poprzednich wyrazów.

Nie zapomnij o deklaracji i wywołaniu funkcji main()!

Przykład wywołania:
---------------------------------------------
Podaj liczbe naturalna: 10
Kolejne 10 liczb w ciągu Fibonacciego to:
0 1 1 2 3 5 8 13 21 34
'''

def main():
    n = int(input("Podaj liczbe naturalna: ")) # 1
    poprzednik = 0 # 1
    nastepnik = 1 # 1
    print("Kolejne",n,"liczb w ciągu Fibonacciego to:")
    if n >= 1:    # 2
        print(poprzednik, end = ' ')
    if n >= 2: # 2
        print(nastepnik, end = ' ')
        
    for i in range(2,n): # 2
        poprzednik, nastepnik = nastepnik, poprzednik+nastepnik # 4
        print(nastepnik, end = ' ') # 2

main()
        

