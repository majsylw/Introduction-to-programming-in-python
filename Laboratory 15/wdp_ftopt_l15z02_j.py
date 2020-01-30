# Wstęp do programowania
# Zaliczenie całościowe
# 30.01.2020 grupa P11-17j
# imię:
# nazwisko:
# indeks:

# Zadanie 2 (15 pkt.)
#
# Napisz program, który pobiera od użytkownika liczbę całkowitą n.
# Następnie program pobiera od użytkownika n liczb rzeczywistych
# i oblicza pierwiastek z sumy ich kwadratów
# (długość wektora w przestrzeni n-wymiarowej):
#         _________________________________
# |A| = \/ (a_1)^2 + (a_2)^2 ... + (a_n)^2

# Wynik zapisz w notacji naukowej, z trzema miejscami po przecinku.

# Przykładowe efekty działania programu:
# =======================================
# Podaj n: 5
# Podaj liczbę: 10
# Podaj liczbę: 15.5
# Podaj liczbę: 20
# Podaj liczbę: 30
# Podaj liczbę: 40
# |A| = 5.692e+01
# =======================================

def main():
    n=int(input("Podaj liczbę całkowitą: ")) # 1
    wynik = 0 # 2
    for i in range (n): # 2
        x = float(input("Podaj liczbę: ")) # 2
        wynik += x**2 # 2
    wynik = wynik**0.5 # 3

    print("|A| = ", format(wynik, ".3e")) # 3

main()
