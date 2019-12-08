'''
Napisz program pozwalający obliczyć wskaźnik BMI (body mass index).
'''

def wskazink_BMI(waga,wzrost):
    BMI = waga/(wzrost**2)
    return BMI

def main():
    m = float(input("Podaj wage: "))
    h = float(input("Podaj wzrost: "))
    wsk_BMI = wskazink_BMI(m,h)
    print("BMI = ", format(wsk_BMI,".1f"))

main()
