'''
Zadanie 5
Napisz program, który sprawdza, czy liczba podana przez użytkownika
jest rozwiązaniem równania x^2 – 2 = 0, z dokładnością do 1e-4.
Program prosi użytkownika o podanie liczby dopóty,
dopóki nie uzyska prawidłowej odpowiedzi.

'''

def main():
    rozwiazanie = 0 # 1 punkt
    while abs(rozwiazanie**2 - 2) > 1e-4: # 2 punkty
        rozwiazanie = float(input("Podaj liczbę będącą rozwiązaniem x^2 – 2 = 0: ")) # 1 punkt

    print("Twoja odpowiedź jest wystarczająco dokładna!") # 1 punkt

main()
