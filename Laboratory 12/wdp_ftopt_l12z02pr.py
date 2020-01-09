'''
Napisz program, który będzie generował zadania matematyczne z zakresu dodawania.
Program powinien wyświetlać dwie liczby całkowite (od 0 do 500). Program powinien
prosić użytkownika o podanie wyniku dodawania tych liczb. Jeśli użytkownik poda
poprawny wynik, to program powinien wyświetlić komunikat z gratulacjami,
w przeciwnym przypadku, komunikat z poprawnym wynikiem.
'''

import random

# Funkcja oblicza sumę dwóch liczb.
# I: dwie liczby całkowite
# P: oblicza sumę z zależności: liczba1 + liczba2
# O: obliczona wartość sumy
def suma(liczba1,liczba2):
    return liczba1+liczba2

def main():
    
    print("Teraz będziemy uczyć się dodawania liczb calkowitych (od 0 do 500).")

    choice = "t"
    while choice == "T" or choice == "t":
        a = random.randint(0, 500)
        b = random.randint(0, 500)

        print("Ile to jest",a,"+",b,"?")
        user_ans = int(input(""))
        wynik = suma(a,b)
        
        if user_ans == wynik:
            print("Gratulacje, to jest poprawna odpowiedź!")
        else:
            print("Błąd, poprawną odpowiedzią jest", wynik)
        
        choice = input("Czy chcesz grać dalej? (t/n): ")
    

main()
