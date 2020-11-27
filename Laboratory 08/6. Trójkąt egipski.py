'''
Trójkąt egipski, to trójkąt prostokątny (a^2+b^2=c^2), którego boki są wyrażone
liczbami naturalnymi a, b, c o stosunkach długości a:b:c = 3:4:5.
Napisz program, który będzie sprawdzał czy dany trójkat jest trójkątem egipskim.
W swoim rozwiązaniu wyszczególnij:
- funkcję czy_egipski() która będzie pobierała jako argumenty trzy boki trójkata,
a zwracała prawdę lub fałsz w zależności czy analizowany trójkat jest trójkatem
egipskim (zauważ, że kolejność danych nie musi mieć znaczenia),
- funkcję main() w której poprowadzisz interakcję z użytkownikiem - wczytasz
potrzebne dane (3 długości boków w dowolnej kolejności - tzn. nie wiesz jakie
boki będą kolejno wprowadzane przez użytkownika), sprawdzisz czy trójkąt
zbudowany z owych długości byłby prostokatny, jeśli tak sprawdzisz dodatkowo
czy dany trójkąt byłby trójkątem egipskim. W każdym z mozliwych wariantów
wyświetl na ekranie stosowny komunikat.
Swoje rozwiązanie załącz w pliku *.py.
'''
def czy_egipski(a, b, c):
    if ((a/b == 3/4 and b/c == 4/5 and a/c == 3/5) or
        (a/c == 3/4 and c/b == 4/5 and a/b == 3/5) or
        (b/a == 3/4 and a/c == 4/5 and b/c == 3/5) or
        (b/c == 3/4 and c/a == 4/5 and b/a == 3/5) or
        (c/a == 3/4 and a/b == 4/5 and c/b == 3/5) or
        (c/b == 3/4 and b/a == 4/5 and c/a == 3/5)):
        return True
    else:
        return False
def main():
    a = float(input("Podaj bok: "))
    b = float(input("Podaj bok: "))
    c = float(input("Podaj bok: "))
    if (a**2 + b**2 == c**2 or
        a**2 + c**2 == b**2 or
        c**2 + b**2 == a**2):
        print("Trójkąt jest pitagorejski.")
        if czy_egipski(a, b, c):
            print("Trójkąt jest egipski.")
        else:
            print("Trójkąt nie jest egipski.")
    else:
        print("Trójkąt nie jest pitagorejski.")
main()
