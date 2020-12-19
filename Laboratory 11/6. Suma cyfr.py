'''
Napisz program, który pozwoli na obliczenie sumy cyfr wprowadzonej
przez uzytkownika liczby całkowitej. Na potrzeby tego zadania możesz
założyć, że użytkownik zawsze wpisze liczbę całkowitą (ale uwzględnij,
że może być to liczba ujemna).

Przykładowe wywołania:

Podaj liczbę: 123
Suma jej cyfr wyniesie 6.

Podaj liczbę: -123
Suma jej cyfr wyniesie 6.

Podaj liczbę: 1
Suma jej cyfr wyniesie 1.
'''

def main():
    liczba = input("Podaj liczbe: ")
    suma = 0
    for i in liczba:
        if i == '-':
            continue
        suma += int(i)
    print("Suma jej cyfr wynosi: ", suma)
main()
