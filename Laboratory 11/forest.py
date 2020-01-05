from turtle import *
from ksztalty import *
from random import randint

myPen = Turtle()
myPen.shape("turtle")
myPen.speed(8)

window = turtle.Screen()
window.bgcolor("#FFFFFF")

# rysujemy tlo
draw_circle(myPen, "#69D9FF", 0, -250, 250)

numberOfEmenets = randint(10,20)

# rysujemy trójkatne drzewa
numberOftrees = randint(3,5)
for star in range(0,numberOfEmenets):
  x = randint(-180,5)
  y = randint(-5,5)
  size = randint(100,200)
  if star%2:
    color = "green"
  else:
    color = "#17A589"
  draw_triangle(myPen, color, x, -100+y, size)
  draw_square(myPen, "brown", x+int(size/2), -100+y-15, 15)

# rysujemy kluliste śnieżynki
for star in range(0,numberOfEmenets):
  x = randint(-180,180)
  y = randint(-160,180)
  size = randint(5,10)
  draw_circle(myPen, "white", x, y, size)





# tworzymy napis wesołych świąt  
myPen.penup()
myPen.color("red")
myPen.goto(-250, 180)
myPen.write("Wesołych świąt!", True, font=("Arial", 48, "bold"))
myPen.hideturtle()  

turtle.exitonclick() # wyłączenie okienka poprzez kliknięcie w dowolnym miejscu ekranu

