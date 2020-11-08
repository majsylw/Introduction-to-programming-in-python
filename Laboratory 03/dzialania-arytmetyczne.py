"""
Napisz program który pozwoli na wyznaczenie godziny (w formacie hh:gg)
końca spotkania na podstawie podanej wartości godziny (i minut)
jego początku oraz czasu trwania w minutach. 
"""
def main():
  hour = int(input("Czas startu (godziny): "))
  mins = int(input("Czas startu (minuty): "))
  dura = int(input("Czas trwania (minuty): "))
  
  hour = hour + dura // 60
  mins = mins + dura % 60

  hour = (hour + mins // 60) % 24
  mins = mins % 60

  print(format(hour, "02d"), ":", format(mins, "02d"))
main()
