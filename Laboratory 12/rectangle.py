# do wczytywania jego wymiarów.

# Funkcja oblicza pole prostokąta.
# I: długość i szerkość
# P: oblicza pole z zależności: pole = długość*szerkość
# O: obliczona wartość pola
def area(length, width):
    return length * width

# Funkcja oblicza obwód prostokąta.
# I: długość i szerkość
# P: oblicza obwód z zależności: obwód = 2*(długość+szerkość)
# O: obliczona wartość obwodu
def perimeter(length, width):
    return 2 * (length + width)

# Funkcja pobiera wymiary prostokąta od użytkownika.
# I: brak
# P: wczytanie liczby rzeczywistej podanej przez użytkownika
# O: (długość, szerkość)
def get_dimensions():
    length = float(input('Podaj długość prostokąta: '))
    width  = float(input('Podaj szerokość prostokąta: '))
    return (length, width)
