'''
Napisz program, który pozwoli na obliczenie sumy oraz iloczynu
odwrotności n kolejnych liczb naturalnych bez zera,
dla liczby n wprowadzonej przez uzytkownika. Na potrzeby tego
zadania możesz założyć, że użytkownik jako liczbę n zawsze wpisze
liczbę naturalną.

Przykładowe wywołania:

Podaj liczbę n: 2
Suma odwrotności 2 kolejnych liczb: 1.5
Iloczyn odwrotności 2 kolejnych liczb: 0.5

Podaj liczbę n: 5
Suma odwrotności 5 kolejnych liczb: 2.2833
Iloczyn odwrotności 5 kolejnych liczb: 0.0083

Podaj liczbę n: 1
Suma odwrotności 1 kolejnych liczb: 1
Iloczyn odwrotności 1 kolejnych liczb: 1
'''

def main():
    
    n = int(input('Podaj liczbę n: '))
    suma = 0
    iloczyn = 1
    for i in range(1, n):
        suma += 1/i
        iloczyn *= 1/i
    print('Suma odwrotności', n, 'kolejnych liczb to: ', format(suma, '.4f'))
    print('Iloczyn odwrotności', n, 'kolejnych liczb to: ', format(iloczyn, '.4f'))

main()
