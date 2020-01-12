# Program sprawdzajacy czy dany rok jest rokiem przestepnym

# Funkcja czy_przestepny pobiera liczbe calkowita (rok)
# i w zaleznosci czy odpowiednie warunki sa spelnione
# zwraca prawde badz falsz
def czy_przestepny(rok):
    if (rok%4==0 and rok%100!=0) or rok%400==0:
        return True
    else:
        return False

def main():
    r = int(input("Podaj rok do sprawdzenia: "))

    if czy_przestepny(r):
        print("Podany rok jest przestepny.")
    else:
        print("Podany rok nie jest przestepny.")

main()
