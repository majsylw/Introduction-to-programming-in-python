def main():
    owoce = ['jablko', 'mango', 'marchew', 'banan']
    lista = len(owoce)
    warzywa = []

    name = "marchew"  

    if lista > 0:                            # ">" zamiast "<"
        print("w koszyku mamy:", owoce)
    if name not in owoce:                    # "not in" zamiast "in"
        print(name, "jest owocem!")
    else:                                    # "not warzywa" zamiast "warzywa"
        if not warzywa:
            print(name, "jest warzywem!")    

    if owoce[0] < owoce[1]:                  # "<" zamiast ">"
       print(owoce[0], "rosnie w Polsce.")

main()
