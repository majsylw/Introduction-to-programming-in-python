'''
Napisz program, w którym użytkownik podaje po kolei liczby całkowite
aż do momentu, gdy ich suma przekroczy wartość 10. Na koniec podaj
liczbę wczytanych liczb oraz ich sumę. UWAGA Nie musisz sprawdzać
czy dane wprowadzane przez użytkownika są poprawne (tzn. czy są to
faktycznie liczby całkowite).
'''

def main():
    suma = 0
    zlicz = 0
    while suma < 10:
        i = int(input("Podaj liczbe calkowitą: "))
        suma += i
        zlicz += 1
    print("Ich suma wynosi: ", suma)
    print("Wprowadzono", zlicz, "liczb.")
main()
