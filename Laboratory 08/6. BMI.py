'''
Wskaźnik masy ciała(ang. body mass index, BMI) to współczynnik powstały
przez podzielenie masy ciała podanej w kilogramach przez kwadrat wysokości
podanej w metrach (BMI = m/h^2). Klasyfikacja (zakres wartości)
wskaźnika BMI została opracowana wyłącznie dla dorosłych i nie może być
stosowana u dzieci, a prezentuje się ona następująco:

Niedowaga	     <= 18,5
Waga normalna	     18,5 < BMI <= 24
Lekka nadwaga	     24 < BMI <= 26,5
Nadwaga	             > 26,5
Otyłość I stopnia	30  < BMI <= 35
Otyłość II stopnia	35  < BMI <= 40
Otyłość III stopnia	> 40
Napisz program, który sprawdzi czy podane BMI należy do jednego z 4 wyników:
niedowaga/waga normalna/lekka nadwaga i nadwaga.
Ponadto w przypadku nadwagi dodatkowo chcemy sprawdzić czy mamy doczynienia
z otyłością. W swoim rozwiązaniu wyszczególnij:
-funkcję czy_poprawne() która będzie pobierała jako argumenty masę oraz
wysokość, a zwracała wartość logiczną w zależności od tego czy podane:
wartośc wzrostu będzie należała do przedziału [1, 3] (załóżmy, że wtedy podany
wzrost dorosłej osoby będzie w metrach) oraz,
wartość masy będzie należała do przedziału [30, 300] (załóżmy, że w takich
przedziałach może wystąpić waga dorosłego człowieka).
-funkcję main() w której poprowadzisz interakcję z użytkownikiem - wczytasz
potrzebne dane, sprawdzisz czy są one poprawne i jeżeli tak będzie - wyliczysz
wartość BMI, a następnie podasz interpretację uzyskanego wyniku,
tzn. wydrukujesz na ekran komunikat na temat tego, do którego z czterech
zakresów wartość BMI użytkownika należy i jeżeli osiągnięty został stan nadwagi,
sprawdzisz którego stopnia. W każdym wariancie odpowiedzi postaraj się
aby na ekranie konsoli pojawił się adekwatny komunikat.
Swoje rozwiązanie załącz w pliku *.py.
'''
def czy_poprawne(masa, wzrost):
    if (wzrost >= 1 and wzrost <= 3) and (masa >= 30 and masa <= 300):
        return True
    else:
        return False

def main():
    m = float(input("Podaj wagę w [kg]: "))
    h = float(input("Podaj wzrost w [m]: "))
    if czy_poprawne(m, h):
        BMI = m/h**2
        if BMI <= 18.5:
            print(str(BMI),"- Niedowaga.")
        elif BMI > 18.5 and BMI <= 24:
            print(str(BMI),"- Waga normalna.")
        elif BMI > 24 and BMI <= 26.5:
            print(str(BMI),"- Lekka nadwaga.")
        else:
            print("Nadwaga.")
            if BMI > 30 and BMI <= 35:
                print(str(BMI),"- Otyłość I stopnia.")
            elif BMI > 35 and BMI <= 40:
                print(str(BMI),"- Otyłość II stopnia.")
            elif BMI > 40:
                print(str(BMI),"- Otyłość III stopnia.")
    else:
        print("Wprowadzono niepoprawne dane!")
main()
