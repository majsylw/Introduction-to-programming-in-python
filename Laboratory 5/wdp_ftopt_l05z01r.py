"""
Wstep do programowania
Zaliczenie czastkowe 1
07.11.2019 grupa P11-17j
imie: Maks
nazwisko: Maksimus
indeks: 000000
"""

'''
Zadanie 1 (6 pkt.)
Ponizszy program powinien pytać uzytkownika o imie oraz wiek,
a nastepnie wypisywac na ekranie napis informujący w ktorym roku osiagnie on wiek 100 lat.
Znajduja sie w nim jednak bledy.
Popraw bledy, aby program dzialal prawidlowo.
Opisz wprowadzone zmiany w komentarzach
'''

def oblicz_wiek(wiek, obecny_rok): #nazwy zmiennych, obiektów nie mogą mieć spacji
    rok = (obecny_rok-wiek)+100
    return rok #return powinno znajdować się w funkcji (brakowalo tabulatora/4 spacji)

def main():
    name = input("Jak masz na imie? ")
    age = int(input("Ile masz lat? ")) #funkcje input musimy zrzutowac na wymagany typ
    
    obecny_rok = 2019
    year=oblicz_wiek(age, obecny_rok) # brakowało zmiennej obecny rok, funkcja oblicz_wiek zwraca wartość, którą należało przypisać do zmiennej year
    print(format(name,"s"),"osiagnie wiek 100 lat w roku", format(year,"d"), sep=" ") # poprawa formatowania wypisania na ekran wyniku

main() #wywołanie funkcji main nie może znajdować się w niej samej (usunięcie tabulatora)
