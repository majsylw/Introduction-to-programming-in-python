# Moduł circle.py
# Zawiera definicje funkcji służących do obliczania:
# pola i obwodu koła oraz do wczytywania promienia.

# import modułu math - wykorzystywana wartość math.pi
import math 

# Funkcja oblicza pole koła.
# I: promień
# P: oblicza pole z zależności: pole = pi*r^2
# O: obliczona wartość pola
def area(radius):
    return math.pi * radius ** 2

# Funkcja oblicza obwód koła.
# I: promień
# P: oblicza obwód z zależności: obwód = 2*pi*r
# O: obliczona wartość obwodu
def circumference(radius):
    return 2 * math.pi * radius

# Funkcja pobiera promień koła od użytkownika.
# I: brak
# P: wczytanie liczby rzeczywistej podanej przez użytkownika
# O: promień
def get_radius():
    return float(input('Podaj promień: '))
