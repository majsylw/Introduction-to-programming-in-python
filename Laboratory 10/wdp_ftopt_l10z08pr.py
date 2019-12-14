'''
Spróbuj wyświetlić choinkę z trójkątów w taki sposób, aby każdy poziom choinki był o 1
wiersz dłuższy.
'''

# trójkąt prostokatny z #
def rysuj_trojkat(h):
    
    for i in range(1,h+1):
        for j in range(1,i+1):
            print('#',end=" ")
        print("",end="\n")
        
def main():
    
    print("Rysujemy choinke")
    wysokosc = int(input("Podaj wysokosc choinki: "))
    for i in range(2,wysokosc+2):
        rysuj_trojkat(i)
    

main()
