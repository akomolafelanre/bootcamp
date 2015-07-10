import turtle


def draw_polygon(pen, n, m):
  total_angle = 180*(int(n)-2)
  angle = total_angle/int(n)
  for a in range(0,m):
    pen.up()
    b = pen.xcor()
    c = b + 100.00
    pen.setx(c)
    for i in range(0,n):
      pen.down()
      pen.forward(50)
      pen.right(180-angle)

def draw_flower(pen):
  for i in range(0,36):
    pen.right(10)
    for i in range(0,2):
      pen.down()
      pen.forward(180)
      pen.right(90)
      pen.forward(40)
      pen.right(90)
      pen.forward(180)
      pen.right(90)
      pen.forward(40)
  pen.forward(5)
  pen.right(90)
  pen.forward(400)
  pen.right(90)
  pen.forward(10)
  pen.right(90)
  pen.forward(400)
  pen.right(90)
  pen.forward(4)
  pen.right(90)
  pen.forward(400)
  pen.right(90)
  pen.forward(8)
  pen.right(90)
  pen.forward(400)
  pen.right(90)


def draw_shapes():
  window = turtle.Screen()
  window.bgcolor("blue")
  pen = turtle.Turtle()
  pen.shape("turtle")
  pen.color("red")
  pen.speed(10)
  pen.up()
  pen.goto(-200,100)
  q = raw_input("How many sides do you want you polygon to have: ")
  r = raw_input("How many polygons do you want: ")

  draw_flower(pen)
  s = pen.xcor() + 200
  pen.up()
  pen.setx(s)
  pen.down()
  draw_polygon(pen, int(q),int(r))
  window.exitonclick()

draw_shapes()