'''
Przyjmijmy, że klasyfikacja (zakres wartości) ludzkiego wzrostu prezentuje się
następująco:
Niski	             <= 170
    Karzeł	       < 150
    Bardzo niski       151 – 160
    Raczej niski       161 – 170
Średni	   	     171 – 180
Wysoki	             181 – 190
Bardzo wysoki	     191 – 220
Napisz program, który sprawdzi czy podany wzrost w cm należy do jednego z 6
przedziałów karzeł/bardzo niski/niski/średni/wysoki/bardzo wysoki. Ponadto
w przypadku gdy podana wartość wzrostu nie będzie należeć do żadnego z przedziałów
program powinien wypisać "Czy na pewno podałeś poprawną liczbę?" i zakończyć
działanie. W swoim rozwiązaniu wyszczególnij:
funkcję czy_w_cm() która będzie pobierała jako argument wyskokość, a zwracała
wartośc logiczna w zależności od tego czy podana wysokość będzie większa
od 80 cm (średni wzrost dziecka dwulatka)
funkcję main() w której poprowadzisz interakcję z użytkownikiem - wczytasz
potrzebne dane, sprawdzicz czy wzrost został podany w centymetrach uzywając
funkcji czy_w_cm(), a następnie jeśli tak będzie podaj interpretację uzyskanego
wyniku, tzn. wydrukuj na ekran komunikat na temat tego, do którego z czterech
zakresów wartość wzrostu użytkownika należy. Dodatkowo gdy wzrost użytkownika
wpadnie do przedziału "Niski" - podaj jego podklasyfikację (czyli jeszcze napisz
czy nalezy do kategorii: karzeł/bardzo niski/raczej niski). Jeżeli podana
wartość wzrostu nie będzie należeć do żadnego z przedziałów program powinien
wypisać "Czy na pewno podałeś poprawną liczbę?" i zakończyć działanie.
W każdym wariancie odpowiedzi postaraj się aby na ekranie konsoli pojawił się
adekwatny komunikat.
Swoje rozwiązanie załącz w pliku *.py.
'''
def czy_w_cm(wzrost):
    if wzrost >= 80 and wzrost <= 220:
        return True
    else:
        return False

def main():
    w = float(input("Podaj wzrost w [cm]: "))
    if czy_w_cm(w):
        if w <= 170:
            print(str(w),"- Niski.")
            if w <= 150:
                print(str(w),"- Karzeł.")
            elif w > 150 and w <= 160:
                print(str(w),"- Bardzo niski.")
            elif w > 160 and w <= 170:
                print(str(w),"- Raczej niski.")
        elif w > 170 and w <= 180:
            print(str(w),"- Średni.")
        elif w > 180 and w <= 190:
            print(str(w),"- Wysoki.")
        else:
            print(str(w),"- Bardzo wysoki.")
    else:
        print("Wprowadzono niepoprawne dane!")
main()
