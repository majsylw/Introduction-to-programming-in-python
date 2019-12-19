# Moduł do rysowania kształtów 
# Zawiera funkcje pozwalające żółwiowi malować określone figury geometryczne

import turtle

# rysowanie koła o zadanym promieniu, położeniu środka (x,y) oraz kolorze (str)
def draw_circle(turtle, color, x, y, radius):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(radius)
  turtle.end_fill()

# rysowanie trójkąta równobocznego o zadanym boku, położeniu lewego wierzchołka (x,y) oraz kolorze (str)
def draw_triangle(turtle, color, x, y, side):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()

  # tutaj rysujemy 3 boki
  for i in range (3):
    turtle.forward(side)
    turtle.left(120)
  turtle.end_fill()
  turtle.setheading(0)

# rysowanie kwadratu o zadanym boku przy ustaleniu położenia lewego dolnego wierzchołka
def draw_square(turtle, color, x, y, side):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()

  # tutaj rysujemy 4 boki
  for i in range (4):
    turtle.forward(side)
    turtle.left(90)
  turtle.end_fill()
  turtle.setheading(0)

# rysujemy prostokąt o zadanej szerokości i wysokości
def draw_rectangle(turtle, color, x, y, width, height):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  for i in range (2):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    
  turtle.end_fill()
  turtle.setheading(0)  

# rysujemy gwiazdę pięcioramienną o zadanym rozmiarze boku 
def draw_star(turtle, color, x, y, size):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.right(144)
  for i in range(5):
    turtle.forward(size)
    turtle.right(144)
    turtle.forward(size)
  turtle.end_fill()
  turtle.setheading(0)
