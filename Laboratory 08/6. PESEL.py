'''
Numer PESEL jest to 11-cyfrowy stały symbol numeryczny jednoznacznie
identyfikujący określoną osobę fizyczną. Zbudowany jest z następujących
elementów: zakodowanej daty urodzenia, liczby porządkowej, zakodowanej płci
oraz cyfry kontrolnej. Informacja o płci osoby, której zestaw informacji jest
identyfikowany, zawarta jest na 10. (przedostatniej) pozycji numeru PESEL:
cyfry 0, 2, 4, 6, 8 – oznaczają płeć żeńską,
a cyfry 1, 3, 5, 7, 9 – oznaczają płeć męską.
Napisz program, który zidentyfikuje płeć użytkownika na podstawie wprowadzonego
z klawiatury numeru PESEL. W tym celu wyszczególnij:
- funkcję czy_poprawny() która będzie pobierała podany PESEL, a zwracała prawdę
lub fałsz w zależności czy podana liczby jest jedenastocyfrowa - zakładamy,
że pierwsza cyfra PESELu to liczba naturalna z przedziału obustronnie
domkniętego [1, 9].
- funkcję czy_mężczyzna() (lub czy_kobieta() jeśli tak wolisz) która będzie
pobierała podany PESEL, a zwracała prawdę lub fałsz w zależności czy
przedostatnia cyfra liczby jest parzysta.
- funkcję main() w której poprowadzisz interakcję z użytkownikiem - wczytasz
potrzebne dane, sprawdzisz czy podany PESEL jest poprawny i jeśli tak to
sprawdzisz jaka jest płeć legitymowanej osoby. W każdym wariancie odpowiedzi
postaraj się aby na ekranie konsoli pojawił się adekwatny komunikat.
Swoje rozwiązanie załącz w pliku *.py.
'''
def czy_mezczyzna(PESEL):
    przed_ostatnia = PESEL%100//10
    if przed_ostatnia % 2:
        return True
    else:
        return False

def main():
    p = int(input("Podaj PESEL: "))
    if len(str(p)) == 11:
        if czy_mezczyzna(p):
            print("Osobnik jest mężczyzną.")
        else:
            print("Osobnik jest kobietą.")
    else:
        print("Niepoprawny PESEL")
main()
