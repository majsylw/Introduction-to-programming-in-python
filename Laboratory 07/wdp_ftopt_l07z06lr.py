# Napisz program, ktory pobiera od uzytkownika pseudonimy 4 osob,
# a nastepnie wyewietla je w porzadku alfabetycznym.

# Na ile sposobow mozemy uszeregowac 4 osoby?
# odpowiedz na 4! = 24 -> czyli mamy 24 mozliwosci ustawien pseudonimow (kazdy print to inne ustawienie)

def main():
    p1 = input("Podaj pierwszy pseudonim: ")
    p2 = input("Podaj drugi pseudonim: ")
    p3 = input("Podaj trzeci pseudonim: ")
    p4 = input("Podaj czwarty pseudonim: ")

    if p1<p2 and p1<p3 and p1<p4:
        if p2<p3 and p2<p4:
            if p3<p4:
                print(p1,p2,p3,p4)
            else:
                print(p1,p2,p4,p3)
        elif p3<p2 and p3<p4:
            if p2<p4:
                print(p1,p3,p2,p4)
            else:
                print(p1,p3,p4,p2)
        elif p4<p2 and p4<p3:
            if p2<p3:
                print(p1,p4,p2,p3)
            else:
                print(p1,p4,p3,p2)
    if p2<p1 and p2<p3 and p2<p4:
        if p1<p3 and p1<p4:
            if p3<p4:
                print(p2,p1,p3,p4)
            else:
                print(p2,p1,p4,p3)
        elif p3<p1 and p3<p4:
            if p1<p4:
                print(p2,p3,p1,p4)
            else:
                print(p2,p3,p4,p1)
        elif p4<p1 and p4<p3:
            if p1<p3:
                print(p2,p4,p1,p3)
            else:
                print(p2,p4,p3,p1)
    if p3<p2 and p3<p1 and p3<p4:
        if p2<p1 and p2<p4:
            if p1<p4:
                print(p3,p2,p1,p4)
            else:
                print(p3,p2,p4,p1)
        elif p1<p2 and p1<p4:
            if p2<p4:
                print(p3,p1,p2,p4)
            else:
                print(p3,p1,p4,p2)
        elif p4<p2 and p4<p1:
            if p2<p3:
                print(p3,p4,p2,p1)
            else:
                print(p3,p4,p1,p2)
    if p4<p2 and p4<p3 and p4<p1:
        if p2<p3 and p2<p1:
            if p3<p1:
                print(p4,p2,p3,p1)
            else:
                print(p4,p2,p1,p3)
        elif p3<p2 and p3<p1:
            if p2<p1:
                print(p4,p3,p2,p1)
            else:
                print(p4,p3,p1,p2)
        elif p1<p2 and p1<p3:
            if p2<p3:
                print(p4,p1,p2,p3)
            else:
                print(p4,p1,p3,p2)
main()
