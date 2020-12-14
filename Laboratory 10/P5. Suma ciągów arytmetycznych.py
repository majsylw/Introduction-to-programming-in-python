'''
Napisz funkcje, które dla podanej liczby n ≥ 1 zwrócą w wyniku odpowiednio: sumę liczb od
1 do n, sumę liczb parzystych od 2 do n, sumę liczb nieparzystych od 1 do n. W tym celu
skorzystaj ze znanych Ci pętli. Napisz program, w którym użytkownik zadecyduje, która z
funkcji zostanie wywołana. Wyświetl uzyskany wynik na ekranie.
'''

# funkcja pobiera n oraz wybor (czyli konfiguracje, dla jakiej ma zostac policzona suma)
def suma_ciagu(n,wybor):
    suma = 0
    if wybor == 1: # zsumowanie wszystkich cyfr z zakresu 1 do n
        for i in range(1,n+1):
            suma += i
    elif wybor == 2: # wybor zsumowania cyfr parzystych z zakresu 1 do n

        for i in range(2,n+1,2):
            suma += i

    elif wybor == 3: # wybor zsumowania cyfr nieparzystych z zakresu 1 do n
        for i in range(1,n+1,2):
            suma += i
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