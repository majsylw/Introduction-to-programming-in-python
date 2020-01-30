# Wstęp do programowania
# Zaliczenie całościowe
# 30.01.2020 grupa P11-17j
# imię:
# nazwisko:
# indeks:

# Zadanie 3 (10 pkt.)

# Korzystając ze zdefiniowanych poniżej funkcji
# uzupełnij ciało funkcji KonwerterTemperatury()

# Funkcja ma spełniać następujące zadania:
#  1. pobierać z klawiatury temperaturę w [K]
#  2. wyznaczać wartości temperatur w [C] oraz [F]
#  3. wyświetlać temperatury w [K],[C],[F]
#  4. zwracać pobraną temperaturę w [K] z klawiatury

# Przykład działania programu:
# ```
# Podaj temperaturę [K]: 7
# ==========================
# T =   +7.00 [K]
# T = -266.15 [C]
# T = -447.07 [F]
# ```

# W funkcji KonwerterTemperatury() możesz
# korzystać z tworzenia zmiennych (operator =),
# wszystkich funkcji zdefiniowanych w tym pliku,
# funkcji print() oraz słowa kluczowego return. 
# Nie przejmuj się jeśli nie rozumiesz niektórych
# poleceń w zdefiniowanych funkcjach, pamiętaj,
# że zawsze możesz przetestować działanie
# poszczególnych funkcji.

# I: tekst > komunikat o błędzie do wyświetlenia
# P: wyświetlenie komunikatu
# O: -
def BledneDane(tekst=''):
    print("Podano błędne dane!",tekst)

# I: -
# P: wczytanie temperatury [K] z klawiatury
# O: temperatura [K]
def WczytajTemperature():
    T = input('Podaj temperaturę [K]: ')
    try:
        T = float(T)
        if T>=0:
            return T
        else:
            BledneDane("T < 0!")
            return WczytajTemperature()
    except:
        BledneDane()
        return WczytajTemperature()

# I: temperatura [K]
# P: zamiana temperatury na Celsjusze
# O: temperatura [C]
def KelwinyNaCelsjusze(T):
    return T - 273.15

# I: temperatura [K]
# P: zamiana temperatury na Fahrenheity
# O: temperatura [F]
def KelwinyNaFahrenheity(T):
    return 32. + 9./5. * KelwinyNaCelsjusze(T)

# I: T > wartość temperatury, skala > skala temperatury
# P: wyświetlanie temperatury
# O: -
def WyswietlTemperature(T,skala='[K]'):
    T_format = f"{T:+7.2f}"
    print(f"T = {T_format} {skala}")

# I: n > liczba znaczków do wyświetlenia
# P: mnożenie '=' razy n
# O: string (np. ==========)
def Linia(n=26):
    return n*'='

###############################################
# Stwórz ciało funkcji KonwerterTemperatury()
def KonwerterTemperatury():
    T=WczytajTemperature()
    print(Linia())
    WyswietlTemperature(T,skala='[K]')
    WyswietlTemperature(KelwinyNaCelsjusze(T), "[C]")
    WyswietlTemperature(KelwinyNaFahrenheity(T), "[F]")
    
    return T
# Przykładowa punktacja:
# [4 pkt] program dziala, ale niekoniecznie wg. reguł zadania
# [1 pkt] wykorzystanie WczytajTemperature()
# [1 pkt]    - | | -    WyswietlTemperature() dla Kelwinów
# [1 pkt]    - | | -    Linia()
# [1 pkt] wyświetlenie  KelwinyNaCelsjusze() 
# [1 pkt]    - | | -    KelwinyNaFahrenheity()
# [1 pkt] wykorzystanie return T
###############################################


def main():
    KonwerterTemperatury()

main()
