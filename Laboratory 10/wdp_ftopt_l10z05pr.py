'''
Napisz program, w którym znajdziesz wszystkie liczby ze przedziału (1,20), które dzielą się
bez reszty przez 3. Wypisz je w stosownym komunikacje.
'''

def main():

    for i in range(1,20):
        if i%3 == 0:
            print(i,end=", ")

main()
