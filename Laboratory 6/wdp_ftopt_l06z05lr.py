'''
Napisz program, który rozwiązuje równanie a⋅x
2 + b⋅x + c = 0. Współczynniki równania
(a, b, c) powinny być podane przez użytkownika.
'''

def miejsca_zerowe_trojmianu(a,b,c):
    delta = b**2-4*a*c
    if delta > 0:
        return (-b-delta**0.5)/(2*a), (-b+delta**0.5)/(2*a)
    elif delta == 0:
        return -b/2/a
    else:
        return 'brak rozwiazan'

def miejsce_zerowe_funkcji_liniowej(a,b):
    if a!= 0:
        x = -b/a
        return x
    else:
        if b == 0:
            return 'nieskonczenie wiele rozwiazan'
        else:
            return 'brak rozwiazan'

def main():
    a = float(input('Podaj wspolczynnik a: '))
    b = float(input('Podaj wspolczynnik b: '))
    c = float(input('Podaj wspolczynnik c: '))

    if a != 0:
        print('Rozwiazanie to: ', miejsca_zerowe_trojmianu(a,b,c))
    else:
        print('Rozwiazanie to: ', miejsce_zerowe_funkcji_liniowej(b,c))



main()
