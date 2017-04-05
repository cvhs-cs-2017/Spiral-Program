import turtle
wn = turtle.Screen()

p = 10  #this can change the size of the initial square
y = 5 #this changes the distance between the lines of the spiral

hi = turtle.Turtle()
hi.speed(0)
a = 0 
b = p
hi.pu()
hi.goto(a,b)


c = p
d = 0

hi.pd()
hi.goto(c,d)

e = -p
f = 0
hi.goto(e,f)


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



wn.mainloop()
