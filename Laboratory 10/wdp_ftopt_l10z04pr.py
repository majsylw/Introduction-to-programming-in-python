'''
Napisz program, który wylicza średnią arytmetyczną kwadratu liczb podawanych przez
użytkownika. Użytkownik powinien określić ile liczb rzeczywistych chce podać.
'''

def main():
    ile = int(input("Ile chcesz podac liczb? "))
    suma = 0
    for i in range(ile):
        print("Czas na liczbe numer ", i+1, ".", sep='')
        liczba = float(input("Podaj liczbe: "))
        suma += liczba**2
    srednia = suma/ile

    print("Srednia z podanych liczb rzeczywistych wynosi: ", format(srednia, ".2f"))

main()
