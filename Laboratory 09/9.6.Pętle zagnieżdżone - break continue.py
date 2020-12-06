def main():
    while True:
        odp = input("A co jeśli? ")
        if odp.lower() != "pomidor":
            for letter in odp:
                if letter in ['a','o','u','e','i','y']:
                    continue
                print(letter, end="")
            break

main()
