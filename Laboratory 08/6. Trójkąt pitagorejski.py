'''
Trójkąt pitagorejski, to trójkąt prostokątny, którego boki są wyrażone liczbami
naturalnymi a, b, c związanymi warunkiem: a2+b2=c2. Napisz program, który będzie
sprawdzał czy dany trójkat jest prostokątny. W swoim rozwiązaniu wyszczególnij:
- funkcję czy_trójkąt() która będzie pobierała jako argumenty 3 odcinki, a
zwracała prawdę lub fałsz w zależności czy można z nich zbudować trójkat
(suma 2 krótszych boków będzie większa od najdłuższego boku); na przykład
trójkąty da się zbudować z odcinków: [9, 12, 15], [3, 4, 5],
- funkcję main() w której poprowadzisz interakcję z użytkownikiem - wczytasz
potrzebne dane (3 długości boków w dowolnej kolejności - tzn. nie wiesz jakie
boki będą kolejno wprowadzane przez użytkownika), sprawdzisz czy można z nich
zbudować trójkąt, jeśli tak sprawdzisz czy jest on prostokątny. W każdym
z mozliwych wariantów wyświetl na ekranie stosowny komunikat.
Swoje rozwiązanie załącz w pliku *.py.
'''
def czy_trójkąt(a, b, c):
    if (a + b >= c or
        a + c >= b or
        c + b >= a):
        return True
    else:
        return False
def main():
    a = float(input("Podaj bok: "))
    b = float(input("Podaj bok: "))
    c = float(input("Podaj bok: "))
    if czy_trojkat(a, b, c):
        print("Z tych odcinków można zbudować trójkat.")
        if (a**2 + b**2 == c**2 or
            a**2 + c**2 == b**2 or
            c**2 + b**2 == a**2):
            print("Trójkąt jest pitagorejski.")
        else:
            print("Trójkąt nie jest pitagorejski.")
    else:
        print("Z tych odcinków nie można zbudować trójkata.")
main()
