'''
Napisz program drukujący na ekranie liczby w postaci trójkąta. Wysokość (h) wczytujemy z
klawiatury mając na względzie, że ma być ona większa od 0 i mniejsza od 5. Niech wypisywane
w wierszach liczby będą kolejnymi potęgami liczby wpisanej w pierwszej kolumnie.
'''

# trójkąt prostokatny z liczb
def rysuj_trojkat(h):
    
    for i in range(1,h+1):
        for j in range(1,i+1):
            print(i**j,end=" ")
        print("",end="\n")
        
def main():
    
    print("Rysujemy trojkat")
    wysokosc = 0
    while wysokosc <= 0 or wysokosc > 5:
        wysokosc = int(input("Podaj wysokosc trojkata: "))
        if wysokosc <= 0 or wysokosc > 5:
            print("Zle dane, sprobuj raz jeszcze!")
    rysuj_trojkat(wysokosc)
    

main()
