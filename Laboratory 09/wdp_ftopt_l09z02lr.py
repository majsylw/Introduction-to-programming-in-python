'''
Napisz program, który wypisuje na ekran zadaną przez użytkownika liczbę gwiazdek.
'''
# wersja podstawowa
def wiersz_gwiazdek(n):
    for i in range(0,n):
        print("*",end=" ")
    print("",end="\n")
        
# wersja rozszerzona: trójkąt prostokatny z gwiazdek
def rysuj_trojkat(h):
    
    for i in range(1,h+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print("",end="\n")
        
def main():
    print("Narysujemy wiersz z gwiazdek")
    liczba_gwiazdek = int(input("Podaj liczbe gwiazdek: "))
    # wersja podstawowa
    wiersz_gwiazdek(liczba_gwiazdek)
    
    print("Teraz rysujemy trojkat")
    wysokosc = int(input("Podaj wysokosc trojkata: "))
    # wersja rozszerzona
    rysuj_trojkat(wysokosc)
    

main()
