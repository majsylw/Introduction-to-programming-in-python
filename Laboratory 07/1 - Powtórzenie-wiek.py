'''
Napisz program, w którym użytkownik zostanie zapytany o wiek. Jeżeli użytkownik
jest przed 18 wyświetli informację „Użytkownik niepełnoletni” oraz zwróci ile
lat zostało użytkownikowi do pełnoletności. Użytkownikom pełnoletnim wyświetli
informację „Użytkownik pełnoletni”. Dodatkowo sprawdź wtedy czy wiek użytkownika
nie przekracza 100 lat i jeśli tak wyświetl komunikat „200 lat ♫”. W swoim
rozwiązaniu wyszczególnij:
-funkcję czy_poprawny(), która przyjmuje jako argument wiek użytkownika i sprawdza
czy jest on nieujemny - ostatecznie zwraca odpowiednią wartość logiczną,
-funkcję ile_do_pełnoletności(), która przyjmuje jako argument wiek użytkownika
i zwraca ile lat brakuje mu do osiągnięcia 18 lat,
-funkcję main(), w której przeprowadzisz interakcję z uzytkownikiem - pobierzesz
od niego dane o wieku, a następnie sprawdzisz opisane powyżej warunki
pełnoletności. Pamiętaj aby w każdym przypadku wyświetlić stosowny komunikat
oraz o wywołaniu funkcji ile_do_pełnoletności().
Rozwiązanie załącz w postaci pliku *.py.
'''
def ile_do_pełnoletności(wiek):
    return 18 - wiek

def czy_poprawny(wiek):
    if wiek >= 0:
        return True
    else:
        return False

def main():
    w = int(input("Podaj swój wiek: "))
    if czy_poprawny(w):
        if w < 18:
            print("Użytkownik niepełnoletni")
            print("Do pełnoletności jeszcze", ile_do_pełnoletności(w))
        else:
            print("Użytkownik pełnoletni")
            if w > 100:
                print("200 lat ♫")
    else:
        print("Podałeś niepoprawny wiek!.")
main()
