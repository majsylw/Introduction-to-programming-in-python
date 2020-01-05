# Program pokazuje importowanie własnych modułów.
# Program wykorzystuje pliki circle.py oraz rectangle.py.
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

#importowanie własnych modułów
import circle
import rectangle

#definicje stałych do obsługi menu
AREA_CIRCLE_CHOICE         = 1
CIRCUMFERENCE_CHOICE       = 2
AREA_RECTANGLE_CHOICE      = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE                = 5

def main():
    print('Program geometria pozwala obliczyć pole i obwód koła i prostokąta.')

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
5. Zakończ pracę.""")

main()
