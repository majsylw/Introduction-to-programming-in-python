"""
Wstep do programowania
Zaliczenie czastkowe 1
07.11.2019 grupa P11-17j
imie: Maks
nazwisko: Maksimus
indeks: 000000
"""

"""
Zadanie 2 (12 pkt.)
Rownanie Clapeyrona opisuje zwiazek pomiedzy temperatura, cisnieniem i objetoscia gazu doskonalego.
Sformulowane zostalo w 1834 roku przez Benoit Clapeyrona.
Prawo to wyraza sie wzorem:
pV = nRT,
gdzie:
p – cisnienie [Pa],
V – objetosc [m^3],
n – liczba moli gazu,
T – temperatura bezwzględna [K],
R – stala gazowa 8,314 J/(mol·K).

Znajac trzy z czterech parametrow (p, V, n, T) mozna wyznaczyc czwarty.
Napisz program, ktory pobiera od uzytkownika trzy wielkosci,
a nastepnie oblicza czwarta (wybierz dowolna). Otrzymany wynik
zaokraglij do 2 miejsc po przecinku. W swoim rozwiazaniu
wyszczegolnij funkcje przyjmujaca trzy argumenty i zwracajaca
wynik obliczen (przygotuj dla niej tabele IPO) oraz funkcje main().
"""
# Tabela IPO -> 2pkt
# Funkcja wyznaczajaca temperature gazu doskonalego
# wejscie: cisnienie, objetosc, liczba moli gazu
# proces: obliczanie temperatury z przeksztalconego wzoru
# wyjscie: temperatura bezwzgledna (liczba rzeczywista)
def T_Clapeyron(p,V,n): # 1
    R = 8.314
    T = p*V/(n*R) # 1
    return T # 1

def main(): # 1
    cisnienie = float(input("Podaj cisnienie [Pa]: ")) # 1
    objetosc = float(input("Podaj objetosc [m^3]: ")) # 1
    l_moli = float(input("Podaj liczbe moli gazu []: ")) # 1

    temperatura = T_Clapeyron(cisnienie,objetosc,l_moli) # 1

    print("T = ", format(temperatura,".2f"), " K") # 1

main() # 1














