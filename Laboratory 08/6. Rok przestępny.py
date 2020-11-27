'''
Czas jednego obiegu ziemi wokół Słońca wynosi 365 dni 5 godzin i 49 minut
(365.242199 dnia).
W związku z tym faktem wprowadzono do kalendarza tak zwane lata przestępne.
Rok przestępny to taki, który ma 366 zamiast 365 dni. Aby wyznaczyć czy dany
rok jest przestępny stosuje się formułę zgodną z kalendarzem Gregoriańskim
wprowadzonym w 1582 roku przez papieża Grzegorza XIII,
w którym rok przestępny spełnia jeden z następujących warunków:
- jest podzielny przez 4, ale nie jest podzielny przez 100
- jest podzielny przez 400
Napisz program, który będzie sprawdzał czy podany przez użytkownika rok
jest rokiem przestępnym. W tym celu wyszczególnij:
- funkcję czy_przestępny() która będzie pobierała podany rok, a zwracała
prawdę lub fałsz w zależności czy analizowany rok jest rokiem przestępnym,
- funkcję main() w której poprowadzisz interakcję z użytkownikiem - wczytasz
potrzebne dane, sprawdzisz czy podany rok jest przestępny (załóż, że może
to być jeden z kolejnych następnych czterech lat) i jeśli nie będzie
podasz kiedy można się spodziewać kolejnego roku przestępnego.
W każdym wariancie odpowiedzi postaraj się aby na ekranie konsoli pojawił się
adekwatny komunikat.
Swoje rozwiązanie załącz w pliku *.py.
'''

def czy_przestepny(rok):
    if not (rok % 4) and (rok % 100) or not (rok % 400) :
        return True
    else:
        return False
def main():
    rok = int(input("Podaj rok: "))
    if czy_przestepny(rok):
        print("Podany rok jest przestępny!")
    else:
        print("Ten rok nie jest przestępny")
        if czy_przestepny(rok + 1):
            print("Ale przestępnym będzie rok", str(rok + 1))
        elif czy_przestepny(rok + 2):
            print("Ale przestępnym będzie rok", str(rok + 2))
        elif czy_przestepny(rok + 3):
            print("Ale przestępnym będzie rok", str(rok + 3))
        elif czy_przestepny(rok + 4):
            print("Ale przestępnym będzie rok", str(rok + 4))
        else:
            print("A kolejny długo nie nadejdzie.")
            
main()
