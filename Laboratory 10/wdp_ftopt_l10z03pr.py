'''
Napisz program, który poprosi użytkownika o podanie imion i nazwisk, następnie wyświetli na
ekranie napis zawierający stosowne inicjały. Postaraj się zwrócić inicjały w postaci dużych
liter. W przypadku posiadania kilku imion/nazwisk, np. Jan Maciej Karol Wścieklicy, wypisz
ich liczbę.
'''

def main():
    imiona = input("Podaj swoje imiona: ")
    nazwiska = input("Podaj swoje nazwiska: ")

    print(imiona[0], end='. ')
    licznik_imion = 1
    for i in range(len(imiona)-1):
        if imiona[i] == ' ':
            print(imiona[i+1], end = '. ')
            licznik_imion += 1

    print(nazwiska[0], end='. ')
    licznik_nazwisk = 1
    for i in range(len(nazwiska)-1):
        if nazwiska[i] == ' ':
            print(nazwiska[i+1], end = '. ')
            licznik_nazwisk += 1

    print("\nLiczba imion",licznik_imion)
    print("Liczba nazwisk", licznik_nazwisk)

main()
