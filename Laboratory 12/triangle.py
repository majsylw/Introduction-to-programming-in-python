# Moduł triangle.py
# Zawiera definicje funkcji służących do obliczania:
# pola i obwodu trójkata oraz
# do wczytywania jego wymiarów - 3 boków.

from math import sqrt

# Funkcja oblicza pole trójkąta ze wzoru Herona.
# I: długości boków a, b i c
# P: oblicza pole z zależności: pole = sqrt((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c))/4
# O: obliczona wartość pola
def area(a,b,c):
    p = 0.5*(a+b+c)
    return sqrt(p*(p-a)*(p-b)*(p-c))

# Funkcja oblicza obwód trójkąta.
# I: długości boków a, b i c
# P: oblicza obwód z zależności: obwód = a+b+c
# O: obliczona wartość obwodu
def perimeter(a,b,c):
    return a+b+c

# Funkcja sprawdza czy z podanych odcinków można zbudować trójkat.
# I: długości boków a, b i c
# P: sprawdzenie czy suma długości 2 dowolnych boków jest większa od długości trzeciego
# O: True lub False
def check_lengths(a,b,c):
    if a+b > c and a+c > b and b+c>a:
        return True
    else:
        return False

# Funkcja pobiera wymiary trójkąta od użytkownika.
# I: brak
# P: wczytanie liczby rzeczywistej podanej przez użytkownika
# O: (a,b,c)
def get_lengths():
    check = False
    while not check:
        a = float(input('Podaj długość pierwszego boku: '))
        b = float(input('Podaj długość pierwszego boku: '))
        c = float(input('Podaj długość pierwszego boku: '))
        check = check_lengths(a,b,c)
        if not check:
            print("Podane wartości są nieprawidłowe, spróbuj jeszcze raz!")
    return a,b,c


