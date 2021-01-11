# Program pokazuje importowanie własnych modułów.
# Program wykorzystuje pliki circle.py, rectangle.py oraz triangle.py.
#
# Plik circle.py zawiera definicje funkcji:
# - area(radius),
# - circumference(radius),
# - get_radius().
#
# Plik rectangle.py zawiera definicje funkcji:
# - area(length, width),
# - perimeter(length, width),
# - get_dimensions().
#
# Plik triangle.py zawiera definicje funkcji:
# - get_lengths() – zwraca długości trzech boków podane przez użytkownika,
# - area(a,b,c) – zwraca pole powierzchni trójkąta (skorzystaj ze wzoru Herona),
# - perimeter(a,b,c) – zwraca obwód trójkąta o podanych bokach.

#importowanie własnych modułów
import circle
import rectangle
import triangle

#definicje stałych do obsługi menu
AREA_CIRCLE_CHOICE         = 1
CIRCUMFERENCE_CHOICE       = 2
AREA_RECTANGLE_CHOICE      = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE                = 7

AREA_TRIANGLE_CHOICE       = 5
PERIMETER_TRIANGLE_CHOICE  = 6

def main():
    print('Program geometria pozwala obliczyć pole i obwód koła, prostokąta i trójkata.')

    # W pętli while pobierana jest od użytkownika liczba całkowita
    # odpowiadająca wybranej czynności (od 1 do 5), a następnie
    # w bloku if-elif-else odczytywane są dane i wykonywane obliczenia.
    choice = 0 #inicjalizacja zmiennej choice
    while choice != QUIT_CHOICE:
        display_menu() #wyświetlenie menu
        #pobranie wartości od użytkownika
        choice = int(input('Wybierz opcję: '))

        #wybór czynności
        if choice == AREA_CIRCLE_CHOICE:            #pole koła
            radius = circle.get_radius()
            print('Pole koła wynosi',circle.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:        #obwód koła
            radius = circle.get_radius()
            print('Obwód koła wynosi',circle.circumference(radius))
        elif choice == AREA_RECTANGLE_CHOICE:       #pole prosokąta
            (length, width) = rectangle.get_dimensions()
            print('Pole prostokąta wynosi', rectangle.area(length, width))
        elif choice == PERIMETER_RECTANGLE_CHOICE:  #obwód prostokąta
            (length, width) = rectangle.get_dimensions()
            print('Obwód prostokąta wynosi', rectangle.perimeter(length, width))
        elif choice == AREA_TRIANGLE_CHOICE:       #pole trójkąta
            (a,b,c) = triangle.get_lengths()
            print('Pole trójkąta wynosi', triangle.area(a,b,c))
        elif choice == PERIMETER_TRIANGLE_CHOICE:  #obwód trójkąta
            (a,b,c) = triangle.get_lengths()
            print('Obwód trójkąta wynosi', triangle.perimeter(a,b,c))
        elif choice == QUIT_CHOICE:                 #koniec programu
            print('Zakończenie działania programu.')
        else:                                       #wartość spoza listy
            print('Błąd: nieprawidłowa opcja.')

def display_menu():
    print("""
Co chcesz zrobić?
1. Policz pole koła.
2. Policz obwód koła.
3. Policz pole prostokąta.
4. Policz obwód prostokąta.
5. Policz pole trójkąta.
6. Policz obwód trójkąta.
7. Zakończ pracę.""")

main()
