# Kończymy gdy dostajemy 0
odd_numbers = 0
even_numbers = 0

# odpowiedź do sprawdzenia
odp = True
# wpisanie n liczb kończy działanie
while odp:
  # odczyt liczby
  number = int(input("Podaj liczbę: "))
  # sprawdzanie nieparzystości
  if number % 2 == 1:
      # zwiększamy licznik nieparzysty
      odd_numbers += 1
  else:
      # zwiększamy licznik parzysty
      even_numbers += 1
  # pytamy czy koniec
  odp = int(input("Czy kończymy? Jeśli tak wpisz niezerową liczbę, w innym wypadku wpisz 0. "))  

# Pokaż wynik
print("Nieparzyste:", odd_numbers)
print("Parzyste:", even_numbers)
