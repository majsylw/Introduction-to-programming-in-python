'''
Napisz program, w którym użytkownik podaje po kolei liczby całkowite
aż do momentu, gdy bezwzględna różnica między dwiema kolejno wczytanymi
liczbami będzie mniejsza od 5. Na koniec podaj liczbę wczytanych
liczb oraz ich sumę. UWAGA Nie musisz sprawdzać czy dane wprowadzane
przez użytkownika są poprawne (tzn. czy są to faktycznie liczby całkowite).
'''
def main():
    liczba = int(input("Podaj liczbę: "))
    i = 1
    suma = liczba
    abs_diff = 5
    while abs_diff > 4:
        kolejna = int(input("Podaj kolejną liczbę: "))
        abs_diff = abs(liczba - kolejna)
        liczba = kolejna
        i += 1
        suma += kolejna
    print("Liczba podanych liczb:", i)
    print("Suma podanych liczb:", suma)
main()
