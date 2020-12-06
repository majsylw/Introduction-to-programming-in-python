# Kończymy gdy dostajemy 0

odd_numbers = 0
even_numbers = 0

# odczytaj pierwszą liczbę
number = int(input("Podaj pierwszą liczbę lub 0 aby zakończyć: "))

# 0 kończy działanie
while number != 0:
  # sprawdź nieparzystość
  if number % 2 == 1:
      # zwiększamy licznik nieparzysty
      odd_numbers += 1
  else:
      # zwiększamy licznik parzysty
      even_numbers += 1
  # odczyt kolejnej liczby
  number = int(input("Podaj kolejną liczbę lub 0 aby zakończyć: "))

# Pokaż wynik
print("Nieparzyste:", odd_numbers)
print("Parzyste:", even_numbers)
