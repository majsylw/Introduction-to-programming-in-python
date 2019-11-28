"""
Wstep do programowania
Zaliczenie czastkowe 2
28.11.2019 grupa P11-57j
imie: Maksymilnian
nazwisko: Maksimus
indeks: 000000
"""

'''
Zadanie 2 ( 10pkt.)
Bobby, po zapoznaniu się z prawem de Broglie'a,
zmartwil sie, ze moze ulec dyfrakcji po przejsciu przez 70-centymetrowe drzwi.
Według prawa de Broglie’a dualizmu korpuskularno-falowego
kazdy obiekt materialny moze być opisywany na dwa sposoby:
jako zbiór cząstek albo jako fala. Konsekwencja tego obserwuje się
efekty potwierdzające falową naturę materii w postaci dyfrakcji
cząstek elementarnych, a nawet całych jąder atomowych.
Prawo de Broglie'a wyznacza sie wzorem:
d * m * v = h,
gdzie:
d – szerokosc szczeliny [m],
m – masa [kg],
v – predkosc [m/s],
h – stala Plancka 6,62607015*10^-34 kg*m^2/s.

Napisz program, ktory pobierze od uzytkownika jego mase i predkosc,
z jaka sie porusza. Nastepnie wyznaczy predkosc z jaka musiaby sie on poruszac
aby ulec rozszczepieniu na 70 cm szczelnie. Na koniec wyswietl stosowny komunikat
w zaleznosci od tego czy wykorzystywana predkosc jest na tyle duza aby doszlo do dyfrakcji.
Dodatkowo wyswietl obliczona predkosc w notacji naukowej w zaokragleniu do 2 miejsc po przecinku.

W swoim rozwiazaniu wyszczegolnij funkcje przyjmujaca 2 argumenty (mase i szerokosc szczeliny) i zwracajaca
wynik obliczen (predkosc).

'''

def predkosc(m,d): # 1
    h = 6.62607015*1e-34 # 1
    return h/(d*m) # 1
    
def main():
    d = 0.7 #.5
    masa = float(input("Podaj swoja mase [kg]: ")) #.5
    p = float(input("Podaj swoja predkosc [m/s]: "))#.5
    wynik = predkosc(masa,d)#.5
    
    epsylon = 1e-5
    if p > (wynik + epsylon) or p < (wynik-epsylon): #1
        print("Nie masz sie czego obawiać, przechodz smialo!")#1
        print("Ale jesli pobiegniesz", format(wynik,".2e"),"m/s to sie moze zle skonczyc")#1
    else: #1
        print("Oj, trzeba bylow wiecej jesc!")#1
    
main()
