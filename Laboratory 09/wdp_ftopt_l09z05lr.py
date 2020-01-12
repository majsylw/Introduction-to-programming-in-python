'''
Napisz program, który sprawdza, czy liczba podana przez użytkownika jest
rozwiązaniem równania x2 – 2 = 0, z dokładnością do 10-4. Program prosi użytkownika
o podanie liczby dopóty, dopóki nie uzyska prawidłowej odpowiedzi.
'''

def main():
    print("Program do zgadywania rozwiazania rownania x**2 - 2 = 0.")
    liczba = 0
    while abs(liczba**2-2) >= 1e-4:
        liczba = float(input("Wprowadz wartość x: "))
    
    print("Zgadles :-)")
        
main()
