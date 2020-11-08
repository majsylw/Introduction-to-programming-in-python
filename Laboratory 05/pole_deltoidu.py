"""
Napisz program, który poprosi użytkownika o podanie długości przekątnych deltoidu, a następnie wyświetli informację o jego polu powierzchni (P=pq/2). W swoim rozwiązaniu zawrzyj:
- funkcję main(), w której pozwolisz użtkownikowi na podanie danych z klawiatury,
- funkcję pole_deltoidu(), która pozwoli na obliczenie pola deltoidu, a którą wywołasz w funkcji main(), 
- wyświetlenie wyniku w funkcji main().
"""

def pole_deltoidu(p, q):
    pole = p * q / 2
    return pole

def main():
    print("Ten program pozwala obliczyc pole deltoidu.")
    d1 = float(input("Podaj przekątną deltoidu: "))
    d2 = float(input("Podaj przekątną deltoidu: "))
    p = pole_kwadratu(d1, d2)
    print("Pole deltoidu wynosi", p)

main()
