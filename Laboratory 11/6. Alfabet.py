'''
Napisz program, który pozwoli na wydrukowanie na ekranie 26 znaków alfabetu
łacińskiego zaczynając od z i kończąc na a, czyli w odwróconej kolejności.
Zatrzymaj wyświetlanie kolejnych liter gdy pojawi się litera, na którą zaczyna
się imię użytkownika programu. Umożliw użytkownikowi wproadzenie jego imienia
na początku programu. Na koniec wydrukuj podane przez użytkownika imię.

Uwaga na małe i wielkie litery, metoda upper() wykonana dla napisu podnosi
jego wszystkie litery na wielkie znaki, a lower() na małe litery, np.
'Ala'.lower() # pozwoli na uzyskanie napisu 'ala'

Przykładowe wywołanie:

Podaj swoje imię: Sylwia
z, y, x, w, v, u, t,
Sylwia

Alfabet łaciński:

A	B	C	D	E	F	G	H	I	J
K	L	M	N	O	P	Q	R	S	T
U	V	W	X	Y	Z

'''

def main():
    name = input('Podaj swoje imię: ')
    zlicz = 0
    for i in range(122,96,-1):
        litera = chr(i)
        if name.lower()[0] == chr(i):
            break
        print(chr(i), end=', ')
    print('\n', name, sep='')
    zlicz += 1

main()
