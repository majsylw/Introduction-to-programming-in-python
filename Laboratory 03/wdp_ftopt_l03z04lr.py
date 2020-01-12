'''
Napisz program, który prosi użytkownika o podanie czasu wyrażonego w sekundach
(uwzględniając część ułamkową), a następnie wyświetla informację ile to godzin,
minut, sekund.
'''

def rozdziel_czas(czas_w_sekundach):
    th = int(czas_w_sekundach)//(60*60)
    print("godziny: ", th)
    pozostale_sekundy = czas_w_sekundach - th*60*60
    print("minuty: ", int(pozostale_sekundy//60))
    print("sekundy: ", pozostale_sekundy%60)

    

def main():
    t = float(input("Podaj czas w sekundach: "))
    rozdziel_czas(t)

    
main()
