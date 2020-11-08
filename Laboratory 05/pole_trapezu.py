"""
Napisz program, który poprosi użytkownika o podanie długości podstaw oraz wysokości trapezu, a następnie wyświetli informację o jego polu powierzchni.
W swoim rozwiązaniu zawrzyj:
- funkcję main(), w której pozwolisz użtkownikowi na podanie danych z klawiatury,
- funkcję pole_trapezu(), która pozwoli na obliczenie pola trapezu, a którą wywołasz w funkcji main(), 
- wyświetlenie wyniku w funkcji main().
"""
def pole_trapezu(a, b, h):
    return (a + b) * h * 0.5

def main():
    print("Ten program pozwala obliczyc pole trojkata.")
    a = float(input("Podaj dlugosc krótszej podstawy: "))
    b = float(input("Podaj dlugosc dłuższej podstawy: "))
    h = float(input("Podaj dlugosc wysokosci: "))
    
    P = pole_trapezu(a, b, h)
    print("P = 1/2 * (", a,"+", b, ') *', h,"=", format(P, ".2f"))

main()
