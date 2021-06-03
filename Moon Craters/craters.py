#www.101computing.net/lunar-craters-challenge/
import turtle
import math
from random import randint

myPen = turtle.Turtle()
myPen.tracer(0)
screen = turtle.Screen()
screen.bgcolor("#111155")
myPen.color("#888888")
myPen.pensize(5)
myPen.penup()
myPen.goto(0,0)

def drawMoon(x,y,radius):
  myPen.penup()
  myPen.goto(x,y-radius)
  myPen.pendown()
  myPen.fillcolor("#AAAAAA")
  myPen.begin_fill()
  myPen.circle(radius)
  myPen.end_fill()

def drawCrater(x,y,radius):
  myPen.pensize(1)
  myPen.penup()
  myPen.goto(x,y-radius)
  myPen.pendown()
  myPen.fillcolor("#AAAAAA")
  myPen.begin_fill()
  myPen.circle(radius,360)
  myPen.end_fill()

MOON_RADIUS = 160   
drawMoon(0,0,MOON_RADIUS)

for i in range(20):
    distance = MOON_RADIUS
    radius = randint(3,50) 
    while (distance + radius > MOON_RADIUS): 
        x = randint(-MOON_RADIUS,MOON_RADIUS)
        y = randint(-MOON_RADIUS,MOON_RADIUS) 
        distance = math.sqrt(x**2 + y**2)
    drawCrater(x,y,radius)

myPen.hideturtle()
myPen.getscreen().update()  