# Program sprawdzajacy jakiej plci jest uzytkownik na podstawie peselu

# Funkcja pobiera pesel jako lanczuch znakow
# i zwraca prawde jesli posiadaczem peselu jest kobieta
# czyli przedostatnia cyfra gdy jest parzysta
def czy_kobieta(pesel):
    if int(pesel[9])%2==0: # jesli 10 cyfra jest parzysta to osobnik jest kobieta
        return True
    else:
        return False

def main():
    nr_pesel = input("Podaj nr pesel: ")
    if nr_pesel and len(pesel)==11: # sprawdzam czy to co podal uzytkownik jest niepuste i czy zawiera 11 znakow
        if czy_kobieta(nr_pesel):
            print("Dany osobnik jest plci zenskiej.")
        else:
            print("Dany osobnik jest plci meskiej.")
    else:
        print("Podales niepoprawny pesel!")

main()
