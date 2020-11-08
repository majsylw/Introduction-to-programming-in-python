"""
Napisz program, który poprosi użytkownika o podanie długości przekątnej kwadratu (a2–√), a następnie wyświetli informację o jego polu powierzchni. W swoim rozwiązaniu zawrzyj:
- funkcję main(), w której pozwolisz użtkownikowi na podanie danych z klawiatury,
- funkcję pole_kwadratu(), która pozwoli na obliczenie pola kwadratu, a którą wywołasz w funkcji main(), 
- wyświetlenie wyniku w funkcji main().
"""

def pole_kwadratu(d):
    pole = d ** 2 / 2
    return pole

def main():
    print("Ten program pozwala obliczyc pole kwadratu.")
    d = float(input("Podaj przekątną kwadratu: "))
    p = pole_kwadratu(d)
    print("Pole kwadratu równa się", p)

main()
