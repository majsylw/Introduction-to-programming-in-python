# importujemy moduły wbudowane pythona i/lub najpotrzebnijesze funkcje
import turtle
from random import randint

# importujemy wszystkie funkcje z naszego modułu kształty
from ksztalty import *

myPen = turtle.Turtle()
myPen.shape("turtle")
myPen.speed(10)

# scena o rozmiarach -400, 400 dla x i y
turtle.window = turtle.Screen()
# nadajemy scenie granatowy kolor
turtle.window.bgcolor("#00008C")

# rysujemy księżyc
draw_circle(myPen, "white", 170,100,50)
draw_circle(myPen, "#00008C", 150,100,50)

# dodajemy gwiazdy - liczba losowa między 6, a 12
numberOfStars = randint(6,12)
for star in range(0,numberOfStars):
  # polozenie gwiazdy - liczba losowa między -180, a 180 dla x
  # polozenie gwiazdy - liczba losowa między -160, a 180 dla y
  # rozmiar gwiazdy - liczba losowa między 5, a 20 dla x
  x = randint(-180,180)
  y = randint(-160,180)
  size = randint(5,20)
  draw_star(myPen, "white", x, y, size)

# rysujemy choinke
draw_triangle(turtle, "green", -330, -200, 150)
draw_triangle(turtle, "green", -310, -100, 100)
draw_triangle(turtle, "green", -280, -20, 50)

# drukujemy świąteczne pozdrowienia
myPen.penup()
myPen.color("yellow")
myPen.goto(-70, -300)
myPen.write("Wesołych świąt!", True, font=("Arial", 48, "bold"))
myPen.hideturtle()  

turtle.exitonclick() # wyłączenie okienka poprzez kliknięcie w dowolnym miejscu ekranu
