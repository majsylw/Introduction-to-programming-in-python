def main():
    n = int(input("Podaj liczbę ocen: "))
    ocena = 0
    suma = 0
    for i in range(n):
        while ocena not in [2, 3, 3.5, 4, 4.5, 5, 5.5]:
            ocena = float(input(f"Podaj ocenę {i+1}.: "))
            if ocena not in [2, 3, 3.5, 4, 4.5, 5, 5.5]:
                print("Niewłaściwa liczba - spróbuj raz jeszcze!")
        suma += ocena
        ocena = 0
    print("Twoja średnia:", format(suma/n, '.1f'))

main()
