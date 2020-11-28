'''
Pewna klasa uczestniczy w lidze klas. Napisz program obliczający,
ile wynosi liczba punktów (pkt) danej klasy zależnie od uzyskanej frekwencji (f)
i średniej ocen (so) w ostatnim półroczu. Klasa otrzymuje dodatkowe 20 punktów,
jeśli frekwencja jest powyżej 94% (f > 94%) i średnia ocen nie jest mniejsza
niż 4,0 (so >= 4,0). Zdobytą wcześniej liczbę punktów i frekwencję wprowadzaj
z klawiatury, a aktualną liczbę punktów wyświetlaj na ekranie.
Dane: liczba całkowita pkt > 0 oznaczająca punkty wcześniej zdobyte
przez klasę, liczba rzeczywista f > 0 oznaczająca procent frekwencji,
liczba rzeczywista so oznaczająca średnią ocen.
Wyniki: liczba całkowita pkt oznaczająca aktualną liczbę punktów danej klasy.
Opis rozwiązania: W rozwiązaniu trzeba zastosować instrukcję warunkową
z warunkiem złożonym zawierającym operator koniunkcji.
'''
def dodatkowe_pkt(frekwencja, średnia):
    if frekwencja > 0.94 and średnia >= 4.0:
        return True
    else:
        return False

def main():
    frekw = float(input("Wpisz frekwencje w %: "))
    frekw = frekw / 100
    średnia = float(input("Wpisz średnią klasy: "))
    pkt = int(input("Podaj dotychczasowe punkty klasy: "))
    if dodatkowe_pkt(frekw, śr):
        print("Aktualne punkty klasy: ", pkt + 20)
    else:
        print("Aktualne punkty klasy: ", pkt)
main()
