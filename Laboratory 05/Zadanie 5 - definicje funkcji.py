"""
Napisz definicję funkcji srednia3(), która dla trzech liczb
podanych jako jej argumenty, z czym domyślna wartość jednego
z nich powinna wynosić 2) zwróci ich średnią arytmetyczną.
"""
def srednia3(a, b, c=2):
    return (a + b + c) / 3
"""
Zdefiniuj funkcję geo(), która dla podanych trzech parametrów:
n=numer elementu ciągu, q=wartość ilorazu ciągu geometrycznego,
a1=wartość pierwszego elementu ciągu (domyślnie 1),
zwróci n-ty element ciągu geometrycznego an=a1⋅q^(n−1).
"""
def geo(n, q, a1=1):
    an = a1 * q**(n-1)
    return an
"""
Zdefiniuj funkcję aryt(), która dla podanych trzech parametrów:
n=numer elementu ciągu, r=wartość różnicy ciągu arytmetycznego,
a1=wartość pierwszego elementu ciągu (domyślnie 1),
zwróci n-ty element ciągu arytmetycznego an=a1⋅(n-1)⋅r.
"""
def aryt(n, r, a1=1):
    an = a1 * r * (n-1)
    return an
"""
Napisz definicję funkcji iloczyn3(), która dla trzech liczb
(podanych jako jej argumenty,
z czym domyślna wartość dla 2 argumentów powinna wynosić 1) zwróci ich iloczyn.
"""
def iloczyn3(a, b=1, c=1):
    return a * b * c
"""
Napisz definicję funkcji calkowita(), która przyjmuje jeden argument
- liczbę zmiennoprzecinkową - oraz zwraca część całkowitą z tej liczby.
"""
def calkowita(x):
    return int(x)
"""
Napisz definicję funkcji pierwiastek2(), która przyjmuje dwa arumenty
- liczbe pierwiastkowana i stopień pierwiastka - oraz zwraca jej pierwiastek
(domyślnie kwadratowy, czyli dla stopnia=2) liczby rzeczywistej podanej
jako argument. Pamietaj, że b = a^(1/n), gdzie:
n – stopień pierwiastka,
a – liczba podpierwiastkowa,
b – pierwiastek n-tego stopnia z liczby a, wynik pierwiastkowania.
"""
def pierwiastek2(a, n=2):
    b = a ** (1/n)
    return b
"""
Napisz definicję funkcji suma3(), która dla trzech liczb
(podanych jako jej argumenty, domyślnie jeden z nich ma wartość 2.0)
zwróci ich sumę.
"""
def suma3(x, y, z = 2.0):
    return x + y + z
"""
Napisz definicję funkcji buduj_zdanie(), która otrzymuje pojedynczy argument
zawierający napis i drukuje na ekranie zdanie zaczynające się podanym napisem
i kończące się zwrotem " - bo tak napisałem!"
Uwaga - funkcja nie powinna nic zwracać.
"""
def buduj_zdanie(s):
    print(s, "- bo tak napisałem!")
