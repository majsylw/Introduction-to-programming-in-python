def main():
    # zmienna nie moze miec spacji w nazwie
    # brakowalo zamykajacego "
    # funkcje input musimy zrzutowac na wymagany typ - tu int
    a1 = int(input("Podaj liczbe calkowita: "))
    b2 = int(input("Podaj liczbe calkowita: "))

    # funkcja wyswietlajaca komunikat na ekranie nazywa sie print
    # wszystkie znaczniki konwersji powinny tyczyc sie liczb calkowitych
    print(format(a1,"d"),' + ',format(b2,"d"), " = ", format(a1+b2,"d"))

#wywolanie funkcji main nie powinno znajdowac sie w funkcji main
main()


