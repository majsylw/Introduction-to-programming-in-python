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
Przygotuj program, w którego zadaniem będzie wydrukowanie alfabetu
w porządku rosnącym (od a do z). Wykorzystaj informację,
że w kodzie ASCI literom a-z odpowiadają liczby od 65 do 90.
Sformatuj napis wyjściowy tak aby w jednym wierszu znalazły się
3 kolejne litery alfabetu rozdzielone znakiem ;.

Pamiętaj o dobrych praktykach pisania kodu,
tzn. przygotuj funkcję main() oraz jej wywołanie.

Oczekiwany komunikat na ekranie:

Alfabet w porządku rosnacym:
A;B;C
D;E;F
G;H;I
J;K;L
M;N;O
P;Q;R
S;T;U
V;W;X
Y;Z;
'''

def main(): # definicja funkcji main 1pkt
    print("Alfabet w porządku rosnacym:")
    x = 0 # zapewnienie sobie zmiennej do
    for i in range(65, 91): # poprawna pętla 4 pkt
        x+=1
        if x%3: # warunek na ; 2pkt
            print(chr(i), end=";") # poprawna zamiana kodu ASCI na znak 3
        else: # kiedy enter 2 pkt
            print(chr(i), end="\n") # drukowanie komunikatów 2

main() # wywołanie funkcji main 1 pkt
