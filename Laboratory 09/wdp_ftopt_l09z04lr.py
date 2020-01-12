'''
Napisz program, który prosi użytkownika o podanie dodatniej liczby całkowitej,
a następnie wyświetla silnię podanej liczby.
'''

# funkcja do wyznaczania silni
def silnia(n):
    iloczyn = 1
    for i in range(1,n+1):
        iloczyn *= i
    return iloczyn
 
def main():
    liczba = int(input("Podaj liczbe ktorej silnie chcesz obliczyc: "))
    wynik = silnia(liczba)
    print(liczba,"! = ",wynik, sep="")
    
main()
