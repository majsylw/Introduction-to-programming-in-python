"""
Napisz program, który poprosi użytkownika o podanie długości boku oraz wysokości rombu, a następnie wyświetli informację o jego polu powierzchni. W swoim rozwiązaniu zawrzyj:
- funkcję main(), w której pozwolisz użtkownikowi na podanie danych z klawiatury,
- funkcję pole_rombu(), która pozwoli na obliczenie pola rombu, a którą wywołasz w funkcji main(), 
- wyświetlenie wyniku w funkcji main().
"""

def main():
    print("Ten program pozwala obliczyc pole rombu.")
    a = float(input("Podaj dlugosc boku rombu: "))
    h = float(input("Podaj wysokosc rombu: "))
    
    P = pole_rombu(a,h) # przenosi zmienne a i h do funkcji pole_rombu
    print("P =", a,"*", h,"=", format(P, ".2f"))
    
def pole_rombu(bok, wysokosc): # funkcja pobiera argumenty bok i wysokosc
    return bok * wysokosc
    

main()
