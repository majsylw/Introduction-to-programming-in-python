'''
Napisz program, który przelicza podaną przez użytkownika temperaturę w stopniach
Fahrenheita, na temperaturę w stopniach Celsjusza, a następnie wypisuje stosowny
komunikat.
W programie wydziel funkcję, która pobiera temperaturę w stopniach Celsjusza i
wyświetla wyniki.
'''
def wyznacz_temperature():
    # Pytanie o temperature (zacheta do wpisania literalu znakow z klawiatury)
    # zrzutowanie na typ float
    F = float(input("Podaj temperature w stopniach Farenheita: "))
    C = 5/9 * (F-32)
    print("W stopniach Celsjusza to bedzie: ", format(C,".2f"))


def main():
    
    # Wyswietlenie odpowiedzi poprzez wywolanie powyzszej funkcji
    wyznacz_temperature()

main()
