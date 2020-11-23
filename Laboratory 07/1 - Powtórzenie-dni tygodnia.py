'''
Napisz program, który prosi użytkownika o podanie liczby całkowitej od 1 do 7.
W odpowiedzi program powinien wyświetlić dzień tygodnia według poniższej
klasyfikacji:
poniedziałek -> 1
wtorek -> 2
środa -> 3
czwartek -> 4
piątek -> 5
sobota -> 6
niedziela -> 7
W przypadku podania liczby spoza przedziału powinien zostać wyświetlony
komunikat o błędzie. W swoim rozwiązaniu wyszczególnij:
funkcję czy_poprawne(), która przyjmuje jako argument liczbę podaną przez
uzytkownika i sprawdza czy nalezy ona do przedziału [1, 7], jeśli tak zwróci
prawdę, jeśli nie zwróci fałsz;
funkcję main(), w której przeprowadzisz interakcję z uzytkownikiem - pobierzesz
od niego dane o liczbie, sprawdzisz czy jest ona poprawna, jeśli tak to
następnie za pomocą odpowiednich instrukcji warunkowych wyznacz jaki to dzień
tygodnia. Pamiętaj aby wypisać na ekranie adekwatny komunikat w każdym
przypadku.
Rozwiązanie załącz w postaci pliku *.py.
'''

def czy_poprawne(liczba):
    if liczba >= 1 and liczba <= 7:
        return True
    return False

def main():
    dane = int(input('Podaj liczbę: '))
    if czy_poprawne(dane):
        if dane == 1:
            print("Poniedziałek")
        elif dane == 2:
            print("Wtorek")
        elif dane == 3:
            print("Środa")
        elif dane == 4:
            print("Czwartek")
        elif dane == 5:
            print("Piątek")
        elif dane == 6:
            print("Sobota")
        else:
            print("Niedziela")
    else:
        print("Nierozpoznana liczba.")
main()
                  
