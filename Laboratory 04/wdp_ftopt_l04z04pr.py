'''
Napisz program, który poprosi użytkownika o podanie promienia koła, a następnie wyświetli
informację o jego polu i obwodzie.
'''

def kolo(promien):
    pi = 3.14
    obwod = 2*pi*promien
    pole = pi*promien**2
    return pole, obwod

def main():
    r = float(input("Wprowadz promien kola w cm: "))
    p,o = kolo(r)
    print("Obwod = ", format(o,".1f"), "cm")
    print("Pole = ", format(p,".1f"), "cm^2")

main()
