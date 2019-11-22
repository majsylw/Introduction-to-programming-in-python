# Program sprawdzajacy jakiej plci jest uzytkownik na podstawie peselu
# wersja 2 - z liczba calkowita jako argument

# Funkcja pobiera pesel jako liczbe calkowita
# i zwraca prawde jesli posiadaczem peselu jest kobieta
# czyli przedostatnia cyfra gdy jest parzysta
def czy_kobieta(pesel):
    # wyciagamy przedostatnia cyfre peselu, czyli cyfre na miejscu dziesiatek
    reszta = (pesel%100)//10

    if reszta%2==0:
        return True
    else:
        return False

def main():
    nr_pesel = int(input("Podaj nr pesel: "))
    if czy_kobieta(nr_pesel):
        print("Dany osobnik jest plci zenskiej.")
    else:
        print("Dany osobnik jest plci meskiej.")

main()
