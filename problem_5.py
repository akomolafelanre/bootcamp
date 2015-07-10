import turtle

def draw_polygon(n, m):
  total_angle = 180*(int(n)-2)
  angle = total_angle/int(n)
  window = turtle.Screen()
  window.bgcolor("blue")
  pen = turtle.Turtle()
  pen.shape("turtle")
  pen.color("red")
  pen.speed(10)
  pen.up()
  pen.goto(-200,100)
  for a in range(0,m):
    pen.up()
    b = pen.xcor()
    c = b + 100.00
    pen.setx(c)
    for i in range(0,n):
      pen.down()
      pen.forward(50)
      pen.right(180-angle)
  window.exitonclick()

def draw_flower():
  window = turtle.Screen()
  window.bgcolor("blue")
  pen = turtle.Turtle()
  pen.shape("turtle")
  pen.color("red")
  pen.speed(10)
  pen.up()
  pen.goto(-300,100)
  for i in range(0,2):
    pen.right(10)
    for i in range(0,2):
      pen.down()
      pen.forward(50)
      pen.right(45)
      pen.forward(50)
      pen.right(120)
      pen.forward(50)
      pen.right(45)
      pen.forward(50)
  window.exitonclick()

draw_flower()
#draw_polygon(10,5)