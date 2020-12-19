'''
Napisz program, wyznaczający pole kwadratu. Program jako dane (długość boku)
powinien przyjmować wyłącznie liczby dodatnie. Jeśli użytkownik poda liczbę
niedodatnią, to powinien zostać poinformowany, że wymagana jest
liczba dodatnia i poproszony o wykonanie kolejnej próby. Próbę wczytywania
liczby powtarzamy dopóty, dopóki użytkownik nie poda poprawnej odpowiedzi.
W przypadku poprawnej odpowiedzi wyświetl na ekranie wyliczone pole kwadratu.
'''

def main():
    bok = float(input("Podaj długość boku kwadratu: "))
    while bok <= 0:
        bok = float(input("Podałeś niepoprawną wartość, podana liczba musi być dodatnia. Podaj długość boku kwadratu: "))
    print("Pole kwadratu wyniesie: ", bok**2)
main()
