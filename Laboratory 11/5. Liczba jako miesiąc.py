'''
Napisz program, który wczytuje z klawiatury poprawny numer miesiąca,
tzn. liczbę całkowitą z przedziału <1,12> . Zakładamy, że możliwe są
tylko 3 próby podania poprawnego numeru. W przypadku poprawnej odpowiedzi
wyświetl na ekranie napis "Twój miesiąc to " i numer miesiąca,
a w innm wypadku "Nie ma takiego miesiąca!".
'''

def main():
    n = 0
    while n < 3:
        x = int(input("Podaj numer miesiaca: "))
        if x in range(1,13):
            print("Twój miesiąc to:", x)
            break
        else:
            print("Nie ma takiego miesiąca!")
            n += 1
main()
