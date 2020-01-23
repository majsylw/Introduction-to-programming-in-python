# Wstęp do programowania
# Zaliczenie całościowe
# 23.01.2020 grupa P11-17d
# imię:
# nazwisko:
# indeks:

# Zadanie 2 (15 pkt.)

# Napisz program, który wypisuje na ekran kolejne liczby pierwsze.
# Użytkownik ma określić ile ilczb lierwszych ma być wypisane.
# Pamiętaj, że 1 nie jest liczbą pierwszą.
# Wskazówka wykorzystaj dzielenie modulo.
# Liczby wypisz w wierszu oddzielone spacjami.
# Uwaga w zadaniu należy napisać własny algorytm
# sprawdzjący czy liczba jest pierwsza wykorzystujący dzielenie modulo.

# Przykładowe efekty działania programu
# =======================================
# Podaj ile liczb chcesz wypisać: 8
# 2 3 5 7 11 13 17 19

def czypierwsza(n):
    if(n<2):
        return 0
    else:
        for i in range(2,n):
            if n%i==0:
                return False
    return True
# 10pt za poprawny algorytm sprawdzania czy liczba jest pierwsza:
# 4 pt za pętlę, 1 pt za to ze 1 nie jest pierwsze, pozostałe 5 pt za
# to prawidłowe działania w pętli, 3 pt za sprawdzanie podzielności
# 2 pt za prawidłowo użyty return

def main():
    #1pt za poprawne zdefiniowanie zmiennych i wprowadzenie
    # ich z klawiatury
    n=int(input("Podaj ile liczb pierwszych chcesz wypisać: "))
    licz=0
    i=2
    while (licz<n):# za poprawną pętlę 2pt
        if (czypierwsza(i)):
            print(i,end=' ')
            licz=licz+1#założenie licznika na pierwsze liczby 2pt
        i=i+1

main()       
