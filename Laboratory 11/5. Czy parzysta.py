'''
Napisz program, który sprawdza, czy liczba podana przez użytkownika
jest parzysta. Jeśli użytkownik poda liczbę nieparzystą, to powinien
zostać poinformowany, że wymagana jest liczba parzysta i poproszony
o kolejną liczbę. Próbę wczytywania liczby powtarzamy dopóty, dopóki
użytkownik nie poda liczby poprawnej. W przypadku poprawnej odpowiedzi
wyświetl na ekranie połowę (liczba/2) tej liczby.
'''
def main():
    liczba = int(input("Podaj liczbę parzystą: "))
    while liczba%2:
        liczba = int(input("Jeszcze raz. Podaj liczbę parzystą: "))
    print("Połowa tej liczby to:", liczba/2)
            
main()
