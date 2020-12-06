def jedna_linijka(n):
    for i in range(n):
        print('*', end="")

def main():
    h = int(input("Podaj wysokosc trojkąta z gwiazdek: "))
    for i in range(h):
        jedna_linijka(i + 1)
        print("")

main()
