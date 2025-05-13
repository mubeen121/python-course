import turtle 
from turtle import*
wn = Screen()
wn.setup(width=1200,height=680)
t = Turtle ()
wn . bgcolor ('black')
t.speed(50)
colors = ('blue','yellow')
for i in range (200):
    t.pencolor(colors[i%len(colors)])
    t.rt(i)
    t.circle(100,i)
    t.fd(i)
    t.rt(180)
    t.fd(i)
done()