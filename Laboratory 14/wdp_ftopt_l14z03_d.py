# Wstęp do programowania
# Zaliczenie całościowe
# 23.01.2020 grupa P11-17d
# imię:
# nazwisko:
# indeks:

# Zadanie 3 (10 pkt.)

# Korzystając ze zdefiniowanych poniżej funkcji
# uzupełnij ciało funkcji Kalkulator()

# Funkcja ma spełniać następujące zadania:
#  1. pobierać z klawiatury liczbę a
#  2. pobierać z klawiatury liczbę b
#  3. pobierać z klawiatury działanie +,-,*,/
#  4. wykonywać działanie -> wynik
#  5. wyświetlać linię
#  6. wyświetlać a dzialanie b = wynik

# Przykład działania programu:
# ```
# Podaj liczbę a: 4
# Podaj liczbę b: 5
# ==============================
# '+' : a+b
# '-' : a-b
# '/' : a/b
# '*' : a*b
# Wybierz działanie: *
# ==============================
# 4.0 * 5.0 = 20.0
# ```

# W funkcji Kalkulator() możesz
# korzystać z tworzenia zmiennych (operator =),
# wszystkich funkcji zdefiniowanych w tym pliku,
# funkcji print() oraz słowa kluczowego return. 
# Nie przejmuj się jeśli nie rozumiesz niektórych
# poleceń w zdefiniowanych funkcjach, pamiętaj,
# że zawsze możesz przetestować działanie
# poszczególnych funkcji.

# I: nazwa symbolu do wczytania
# P: wczytanie liczby float  z klawiatury
# O: liczba 
def WczytajLiczbe(symbol):
    liczba = input(f"Podaj liczbę {symbol}: ")
    try:
        return float(liczba)
    except:
        print("Zły format!")
        return WczytajLiczbe(symbol)

# I: n > liczba znaczków '='
# P: -
# O: mnożenie n * '=' (np. =========)
def Linia(n=30):
    return n*'='

# I: -
# P: pobieranie działania z klawiatury
# O: działanie
def WybierzDzialanie():
    dodawanie = "'+' : a+b"
    odejmowanie = "'-' : a-b"
    mnozenie = "'*' : a*b"
    dzielenie = "'/' : a/b"
    print(Linia())
    inputText = f"\
{dodawanie}\n\
{odejmowanie}\n\
{dzielenie}\n\
{mnozenie}\n\
Wybierz działanie: " 

    dzialanie = input(inputText)
    if dzialanie in ['+','-','*','/']:
        return dzialanie
    else:
        print("[!] Brak zdefiniowanego dzialania:",dzialanie)
        return WybierzDzialanie()

# I: a, b, dzialanie
# P: wynik = a dzialanie b
# O: wynik
def WykonajDzialanie(a,b,dzialanie):
    if dzialanie == '+':
        return a+b
    elif dzialanie == '-':
        return a-b
    elif dzialanie == '/':
        if b == 0:
            return 'NaN'
        else:
            return a/b
    elif dzialanie == '*':
        return a*b

# I: a,b,dzialanie,wynik
# P: wyświetlenie a,b,dzialanie,wynik
# O: -
def WyswietlWynik(a,b,dzialanie,wynik):
    print(f'{a} {dzialanie} {b} = {wynik}')

def Kalkulator():
    a = WczytajLiczbe('a')
    b = WczytajLiczbe('b')
    dzialanie = WybierzDzialanie()
    wynik = WykonajDzialanie(a,b,dzialanie)
    print(Linia())
    WyswietlWynik(a,b,dzialanie,wynik)    

# Przykładowa punktacja:
# [4 pkt] program dziala, ale niekoniecznie wg. reguł zadania
# [1 pkt] wykorzystanie WczytajImie()
# [1 pkt]    - | | -    WczytajNazwisko()
# [1 pkt]    - | | -    ZrobInicjaly
# [1 pkt]    - | | -    Linia()
# [1 pkt]    - | | -    Wyswietl()
# [1 pkt]    - | | -    return inicjaly


def main():
    Kalkulator()

main()
