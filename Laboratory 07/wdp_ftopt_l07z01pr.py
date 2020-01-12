# program wyznaczajacy podatek dochodowy

def main():
    pensja = int(input("Podaj swoj przychod brutto: "))

    if pensja <= 4000:
        podatek = 0
    elif pensja > 4000 and pensja <=90000:
        podatek = pensja*0.2
    else:
        podatek = pensja*0.3

    print("Podatek dochodowy wyniesie: ", format(podatek,".2f"),"zl")

main()
