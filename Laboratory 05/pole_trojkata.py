"""
Napisz program, który poprosi użytkownika o podanie wysokości i boku trójkata, na który opuszczona jest ta wysokość, a następnie wyświetli informację o jego polu powierzchni. W swoim rozwiązaniu zawrzyj:
- funkcję main(), w której pozwolisz użtkownikowi na podanie danych z klawiatury,
- funkcję pole_trojkata(), która pozwoli na obliczenie pola trójkąta, a którą wywołasz w funkcji main(), 
- wyświetlenie wyniku w funkcji main().
"""
def pole_trojkata(a, h):
    return a * h * 0.5

def main():
    print("Ten program pozwala obliczyc pole trojkata.")
    a = float(input("Podaj dlugosc boku: "))
    h = float(input("Podaj dlugosc wysokosci: "))
    
    P = pole_trojkata(a, h)
    print("P = 1/2 *", a,"*", h,"=", format(P, ".2f"))

main()
