'''
Napisz program, który pozwoli użytkownikowi obliczyć odległość euklidesową między dwoma
punktami (x1, y1) i (x2, y2).
'''

def odleglosc_euklidesowa(x1,y1,x2,y2):
    d = ((x1-x2)**2+(y1-y2)**2)**0.5
    return d

def main():
    P1x = float(input("Wprowadz x1: "))
    P1y = float(input("Wprowadz y1: "))
    P2x = float(input("Wprowadz x2: "))
    P2y = float(input("Wprowadz y2: "))
    odleglosc = odleglosc_euklidesowa(P1x,P1y,P2x,P2y)
    print("Odleglosc miedzy podanymi punktami: ", format(odleglosc,".1f"))

main()
