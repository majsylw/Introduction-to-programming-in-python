def czy_długi_skok(napis):
    if len(napis) == 2:
        if napis[0] == ' ' and (napis[1] == 'w' or napis[1] == 'W' or
                                napis[1] == 's' or napis[1] == 'S' or
                                napis[1] == 'a' or napis[1] == 'A' or
                                napis[1] == 'd' or napis[1] == 'D'):
            return True
    return False

def main():
    dane = input('Wciśnij odpowiednie klawisze: ')
    if dane == 'Q' and dane == 'q':
        print('Chcesz przeładować broń.')
    elif dane == ' ':
        print("Chcesz skoczyć.")
    elif dane == 'D' or dane == 'd':
        print("Chcesz się poruszyć w prawo.")
    elif dane == 'A' or dane == 'a':
        print("Chcesz się poruszyć w lewo.")
    elif dane == 'W' or dane == 'w':
        print("Chcesz się poruszyć w górę.")
    elif dane == 'S' or dane == 's':
        print("Chcesz się poruszyć w tył.")
    else:
        if czy_długi_skok(dane):
            print("Chcesz wykonać długi skok.")
        else:
            print("Nierozpoznany znak.")
main()
                  
