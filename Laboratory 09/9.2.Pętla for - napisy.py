def main():
    napis = input("Podaj swój wyraz: ")
    counter = 0
    for l in napis.lower():
        if l in ['a','o','i','y','e','u']:
            counter += 1
    print("Liczba samogłosek:", counter)

main()
