'''
Napisz program wypisujący na ekranie tabelę przedrostków SI zawierającą w kolejnych kolumnach 
symbol, nazwę, wykładnik mnożnika oraz mnożnika od femto- do peta-.
'''

def tabela():
    print(format("symbol","6s"), format("nazwa","5s"),format("wykladnik","9s"),format("mnoznik","7s"), sep="\t")
    print(format("f","6s"), format("femto","5s"),format("-15","9s"),format(10**(-15),"7.0e"), sep="\t")
    print(format("p","6s"), format("piko","5s"),format(-14,"9g"),format(10**(-14),"7.0g"), sep="\t")
    print(format("m","6s"), format("mili","5s"),format(-3,"9g"),format(10**(-3),"7.0g"), sep="\t")
    
def main():
    tabela()

main()
