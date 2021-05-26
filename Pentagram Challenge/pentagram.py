#www.101computing.net/pentagram-challenge/
#https://replit.com/@PrestonSo4/Pentagram-Challenge-1#main.py
#if you want to see the code in action click above to the repl.it link
import turtle, math
myPen = turtle.Turtle()
myPen.speed(209)
myPen.shape("arrow")
myPen.pencolor("purple")
myPen.pensize(2)
myPen.speed(1000)
def drawPolygon(polygon):
 myPen.penup()
 myPen.goto(polygon[0][0],polygon[0][1]) # goes to the first coord in list
 myPen.pendown() # pendown (starts drawing)
 
 for i in range(1,len(polygon)):
    myPen.goto(polygon[i][0],polygon[i][1]) # goes to the specific x, y coord depending on the part of the shape
 
 myPen.goto(polygon[0][0],polygon[0][1])

pentagon=[]

for n in range(0,5):
  R = 150  
  x = R*math.cos(math.radians(90+n*72)) #outer coords, 90 is the start angle and it increments 72. I need to look up more how the cos and sin works in this
  y = R*math.sin(math.radians(90+n*72))
  pentagon.append([x,y])
  R = 57
  x = R*math.cos(math.radians(126+n*72)) #inner pentagon to make the star shape
  y = R*math.sin(math.radians(126+n*72))
  pentagon.append([x,y])
print(pentagon)
drawPolygon(pentagon)
myPen.hideturtle()
