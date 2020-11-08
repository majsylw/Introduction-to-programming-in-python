"""
Napisz program, który poprosi użytkownika o podanie długości boków prostokata, a następnie wyświetli informację o jego polu powierzchni. W swoim rozwiązaniu zawrzyj:
- funkcję main(), w której pozwolisz użtkownikowi na podanie danych z klawiatury,
- funkcję pole_prostokąta(), która pozwoli na obliczenie pola prostokata, a którą wywołasz w funkcji main(), 
- wyświetlenie wyniku w funkcji main().
"""
def pole_prostokata(a, b):
    return a * b

def main():
    print("Ten program pozwala obliczyc pole prostokąta.")
    a = float(input("Podaj dlugosc pierwszego boku: "))
    b = float(input("Podaj dlugosc drugiego boku: "))
    
    P = pole_prostokata(a, b)
    print("P =", a,"*", b,"=", format(P, ".2f"))

main()
