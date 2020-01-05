from turtle import *
from ksztalty import *
from random import randint

myPen = Turtle()
myPen.shape("turtle")
myPen.speed(8)

window = turtle.Screen()
window.bgcolor("#FFFFFF")

# rysujemy tlo
draw_circle(myPen, "#69D9FF", 0, -200, 200)

# rysujemy kluliste śnieżynki
numberOfStars = randint(10,20)
for star in range(0,numberOfStars):
  x = randint(-180,180)
  y = randint(-160,180)
  size = randint(5,10)
  draw_circle(myPen, "white", x, y, size)

# rysujemy bałwanka
draw_circle(myPen, "white", 0, -195, 70)
draw_circle(myPen, "white", 0, -100, 55)
draw_circle(myPen, "white", 0, -10, 40)

# rysujemy nosek
draw_circle(myPen, "red", 0, 20, 10)
draw_circle(myPen, "white", 0, 25, 10)

# rysujemy oczka
draw_circle(myPen, "black", -15, 40, 5)
draw_circle(myPen, "black", 15, 40, 5)

# rysujemy guziczki
for y in range(-150,-50,30):
  draw_circle(myPen, "black", 0, y, 5)

# rysujemy rączki
myPen.setheading(45)
draw_rectangle(myPen, "brown", -30, -20, 2, 50)
myPen.setheading(-45)
draw_rectangle(myPen, "brown", 30, -20, 2, 50)

# tworzymy napis wesołych świąt  
myPen.penup()
myPen.color("red")
myPen.goto(-250, 180)
myPen.write("Wesołych świąt!", True, font=("Arial", 48, "bold"))
myPen.hideturtle()  

turtle.exitonclick() # wyłączenie okienka poprzez kliknięcie w dowolnym miejscu ekranu

