
# funkcja pobiera n oraz wybor (czyli konfiguracje, dla jakiej ma zostac policzona suma)
def suma_ciagu(n,wybor):
    if wybor == 1: # zsumowanie wszystkich cyfr z zakresu 1 do n
        suma = (1+n)/2*n
    elif wybor == 2: # wybor zsumowania cyfr nieparzystych z zakresu 1 do n
        if n%2 == 0:
            suma = (2+n)/2*(n//2) # gdy n parzyste
        else:
            suma = (2+n-1)/2*(n//2) # gdy n nieparzyste
    elif wybor == 3: # wybor zsumowania cyfr nieparzystych z zakresu 1 do n
        if n%2 == 1:
            suma = (1+n)/2*(n//2+1) # gdy n nieparzyste
        else:
            suma = (1+n-1)/2*(n//2)# gdy n parzyste
    else:
        print("Nie ma takiego wyboru!")
        suma = None # jesli w ostatniej linijce tej funkcji umiescimy instrukce return suma
                    # to w tym miejscu ta zmienna takze musi sie pojawic i przyjac jakas wartosc

    return suma

def main():
    w = int(input("Wybierz konfiguracje.\n 1 - suma wszyskich cyfr\n 2 - suma cyfr parzystych \n 3 - suma cyfr nieparystych\n"))
    n = int(input("Podaj liczbe calkowita n: "))

    if n<1:
        print("Podales niewlasciwa liczbe calkowita.")
    else:
        print("Wynik dla wyboru",w,"wynosi:",suma_ciagu(wybor=w, n=n))

main()
