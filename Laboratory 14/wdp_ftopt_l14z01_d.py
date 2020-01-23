# Wstęp do programowania
# Zaliczenie całościowe
# 23.01.2020 grupa P11-17d
# imię:
# nazwisko:
# indeks:

# Zadanie 1 (15 pkt.)
# Aby zrelaksować się w trakcie kolokwium postanawiasz
# napisać grę "zgadywanka" i zagrać z komputerem.
# Reguły gry:
# - użytkownik próbuje zgadnąć jaką liczbę całkowitą
#   z przedziału [1,10] komputer ma na myśli.

# Program powinien zadać pytanie „Czy chcesz zgadnąć
# moją liczbę całkowitą?” a użytkownik powinien udzielać
# odpowiedzi,
# - jeśli "tak" program powinien zadać pytanie
#   czy wyswietlic podpowiedź,
#   - jesli "tak", to powinien pojawić się komunikat
#     o dozwolonym zakresie [1,10],
#   - następnie niezależnie od tego czy użytkownik
#     zażyczył sobie podpowiedzi, program powinien
#     poprosić o podanie liczby całkowitej
#   - jesli podana liczba jest za duża program powinienen
#     wyświetlić komunikat "Za duża liczba."
#   - jesli podana liczba jest za mała program powinienen
#     wyświetlić komunikat "Za mała liczba."
#   - jesli podana liczba jest dobra program powinienen
#     wyświetlić komunikat "Brawo, zgadłeś moją liczbę."

# Szczegółowe wymogi dotyczace implementacji programu:
# - zainicjalizuj potrzebne zmienne odpowiedniego typu:
#   przechowywaną w pamięci liczbę i odpowiedź użytkownika (2 pkt)
# - poprawnie zaprogramuj interakcje z użytkownikiem - daj
#   mu możliwość wyboru odpowiedzi (2 pkt)
# - skonstruuj odpowiednie warunki sprawdzajace odpowiedzi
#   i kierujące dalsza częścia programu (5 pkt) 
# - przypisz instrukcji else odpowiednie dzialanie (1 pkt)
# - dla każdego możliwego wyniku wypisz odpowiedni komunikat (5 pkt)

# Program będzie oceniany tylko w przypadku,
# gdy będzie można go uruchomić!
# ----------------------------------------------------
# Przykładowe wynik uruchomienia programu:
# ----------------------------------------------------
# Czy chcesz zgadnąć moją liczbę całkowitą? (jeśli tak wcisnij T) T
# Czy wyswietlić podpowiedź? (jeśli tak wcisnij T) T
# Moja liczba jest z przedziału [1,10].
# Podaj liczbę całkowitą: 5
# Moja liczba jest mniejsza, to 1
#----------------------------------------------------
# Czy chcesz zgadnąć moją liczbę całkowitą? (jeśli tak wcisnij T) T
# Czy wyswietlić podpowiedź? (jeśli tak wcisnij T) N
# Podaj liczbę całkowitą: 3
# Moja liczba jest wieksza, to 5
#----------------------------------------------------
# Czy chcesz zgadnąć moją liczbę całkowitą? (jeśli tak wcisnij T) N
# Szkoda, do zobaczenia!
#----------------------------------------------------

import random

def main():
    guess = random.randint(1,10) # 1
    ans = input("Czy chcesz zgadnąć moją liczbę całkowitą? (jeśli tak wcisnij T) ") # 1

    if ans=="T" or ans=="t": # 1
        ans = input("Czy wyswietlić podpowiedź? (jeśli tak wcisnij T) ") # 1
        if ans=="T" or ans=="t": # 1
            print("Moja liczba jest z przedziału [1,10].") # 1
        ans = int(input("Podaj liczbę całkowitą: ")) # 1
        if ans > guess: # 1
            print("Moja liczba jest mniejsza, to",guess) # 1
        elif ans < guess: # 1
            print("Moja liczba jest wieksza, to",guess) # 1
        else: # 1
            print("Brawo, zgadłeś moją liczbę.") # 1
    else: # 1
        print("Szkoda, do zobaczenia!") # 1
        
main()
