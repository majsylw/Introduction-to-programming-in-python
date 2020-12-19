'''
Napisz program, który pozwoli na sprawdzenie czy we wpisanej przez uzytkownika
liczbie całkowitej jest więcej liczb parzystych czy nieparzystych.
Na potrzeby tego zadania możesz założyć, że użytkownik zawsze wpisze
liczbę całkowitą (ale uwzględnij że może być to liczba ujemna).

Przykładowe wywołania:

Podaj liczbę: 123
Ta liczba ma więcej cyfr nieparzystych.

Podaj liczbę: -123
Ta liczba ma więcej cyfr nieparzystych.

Podaj liczbę: 2
Ta liczba ma więcej cyfr parzystych.
'''

def main():
    liczba = input("Podaj liczbę całkowitą: ")
    nieparzyste = 0
    parzyste = 0
    for i in liczba:
        if i == '-':
            continue
        if int(i)%2:
            nieparzyste += 1
        else:
            parzyste += 1
    if parzyste > nieparzyste:
        print("Ta liczba ma więcej cyfr parzystych.")
    elif parzyste == nieparzyste:
        print("Cyfr parzystych i nieparzystych jest tyle samo.")
    else:
        print("Ta liczba ma więcej cyfr nieparzystych.")
main()
