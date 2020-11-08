"""
Napisz program, który poprosi użytkownika o podanie długości trzech boków trójkata, a następnie wyświetli informację o jego polu powierzchni wyliczonej ze wzoru Herona.
W swoim rozwiązaniu zawrzyj:
- funkcję main(), w której pozwolisz użtkownikowi na podanie danych z klawiatury,
- funkcję pole_trojkata(), która pozwoli na obliczenie pola trójkąta, a którą wywołasz w funkcji main(), 
- wyświetlenie wyniku w funkcji main().
"""
def pole_trojkata(a, b, c):
    return (((a + b + c)   *
             (- a + b + c) *
             (a - b + c)   *
             (a + b - c))  ** 0.5) / 4

def main():
    print("Ten program pozwala obliczyc pole trojkata.")
    a = float(input("Podaj dlugosc boku: "))
    b = float(input("Podaj dlugosc boku: "))
    c = float(input("Podaj dlugosc boku: "))
    
    P = pole_trojkata(a, b, c)
    print("P =", format(P, ".2f"))

main()
