import turtle
wn = turtle.Screen()

hi = turtle.Turtle()
hi.speed(0)
a = -15
b = 15
hi.pu()
hi.goto(a,b)

c = 15
d = 15
hi.pd()
hi.goto(c,d)

e = 15
f = -15
hi.goto(e,f)

g = -15
h = -15
hi.goto(g,h)

for i in range(50):
  x = hi.towards(a,b)
  hi.setheading(x)
  hi.goto(a,b)
  hi.fd(7)
  a = hi.xcor()
  b = hi.ycor()
  x = hi.towards(c,d)
  hi.seth(x)
  hi.goto(c,d)
  hi.fd(7)
  c = hi.xcor()
  d = hi.ycor()
  x = hi.towards(e,f)
  hi.seth(x)
  hi.goto(e,f)
  hi.fd(7)
  e = hi.xcor()
  f = hi.ycor()
  x = hi.towards(g,h)
  hi.seth(x)
  hi.goto(g,h)
  hi.fd(7)
  g = hi.xcor()
  h = hi.ycor()


wn.mainloop()
