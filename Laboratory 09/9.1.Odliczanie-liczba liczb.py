# Kończymy gdy dostajemy 0
odd_numbers = 0
even_numbers = 0

# zapytaj o liczbę liczb
n = int(input("Ile chcesz wprowadzić wszystkich liczb? "))

# iterator do odliczania
i = 0
# wpisanie n liczb kończy działanie
while i < n:
  # odczyt liczby
  number = int(input("Podaj liczbę: "))
  # sprawdzanie nieparzystości
  if number % 2 == 1:
      # zwiększamy licznik nieparzysty
      odd_numbers += 1
  else:
      # zwiększamy licznik parzysty
      even_numbers += 1
  # zwiększamy iterator o 1
  i += 1
  

# Pokaż wynik
print("Nieparzyste:", odd_numbers)
print("Parzyste:", even_numbers)
