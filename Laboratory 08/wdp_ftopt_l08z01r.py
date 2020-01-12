"""
Wstep do programowania
Zaliczenie czastkowe 2
28.11.2019 grupa P11-57j
imie: Maksymilnian
nazwisko: Maksimus
indeks: 000000
"""

'''
Zadanie 1 (4 pkt.)
Ponizszy program powinien wypisywac na ekranie komunikat:
w koszyku mamy: ['jablko', 'mango', 'marchew', 'banan']
marchew jest warzywem!
jablko rosnie w Polsce.

Zmien warunki (tylko warunki!) w taki sposb aby bylo to mozliwe.
'''


def main():
    owoce = ['jablko', 'mango', 'marchew', 'banan']
    lista = len(owoce)
    warzywa = []
    name = "marchew"
    
    if lista > 0:
        print("w koszyku mamy:", owoce)

    if name not in owoce:
        print(name, "jest owocem!")
    else:
        if not warzywa:
            print(name, "jest warzywem!")

    
    if owoce[0] < owoce[1]:
        print(owoce[0], "rosnie w Polsce.")

main()
