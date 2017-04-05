import turtle
wn = turtle.Screen()

p = 10  #this can change the size of the initial square
y = 5 #this changes the distance between the lines of the spiral

hi = turtle.Turtle()
hi.speed(0)
a = -p
b = p
hi.pu()
hi.goto(a,b)


c = p
d = p

hi.pd()
hi.goto(c,d)

e = p
f = -p
hi.goto(e,f)

g = -p
h = -p
hi.goto(g,h)

for i in range(100):
  x = hi.towards(a,b)
  hi.setheading(x)
  hi.goto(a,b)
  hi.fd(y)
  a = hi.xcor()
  b = hi.ycor()
  x = hi.towards(c,d)
  hi.seth(x)
  hi.goto(c,d)
  hi.fd(y)
  c = hi.xcor()
  d = hi.ycor()
  x = hi.towards(e,f)
  hi.seth(x)
  hi.goto(e,f)
  hi.fd(y)
  e = hi.xcor()
  f = hi.ycor()
  x = hi.towards(g,h)
  hi.seth(x)
  hi.goto(g,h)
  hi.fd(y)
  g = hi.xcor()
  h = hi.ycor()


wn.mainloop()
