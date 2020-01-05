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

x = 0
y = -80
width = 20

# rysujemy czapkę
draw_triangle(myPen, "red", x-100, y, 200)

# rysujemy pompon
draw_circle(myPen, "white", x, y+150, 20)

# rysujemy opaskę z pomponów
while (x >= -100) and (x <= 200):
  draw_circle(myPen, "white", x-100, y-20, 20)
  x = x + 20

# tworzymy napis wesołych świąt  
myPen.penup()
myPen.color("red")
myPen.goto(-250, 180)
myPen.write("Wesołych świąt!", True, font=("Arial", 48, "bold"))
myPen.hideturtle()  

turtle.exitonclick() # wyłączenie okienka poprzez kliknięcie w dowolnym miejscu ekranu




