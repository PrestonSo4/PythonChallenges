#https://www.101computing.net/triangle-geometry-functions/
from math import sqrt
def getPerimeter(a,b,c):
    perimeter = a+b+c
    print("The perimeter of a triangle with sidelengths: " + str(a) + ", "+ str(b) + ", "+ str(c) + ", will have a perimeter of:", perimeter)
def getArea(b, h):
    area = b*h/2
    print("The area of a triangle with a baselegth of:", b, "and a height of:", h, "will be:", area)
def getAngles(a1, a2):
    if a1 + a2 > 180:
        print("Those are invalid angles for a triangle")
    else:
        a3 = 180 - a1 - a2
        print("The final angle of a triangle with angles:", a1, "and", a2, "will be:", a3)
def isEquilateral(a,b,c):
    if a == b and a == c:
        print("The triangle with all sidelengths of:", a, "is an equilateral triangle.")
    else:
        print("Your triangle with the specified information is not an equilateral tirangle")
def isIsoscles(a,b,c):
    if a == b or a == c or b == c:
        print("A triangle with the sideslengths of:",str(a) + ",",str(b) + ",",str(c) + ", is an Isoscles triangle.")
    else:
        print("Your triangle with the specified information is not an isoscles tirangle")        
def pythagTheorem():
    q = input("Are you solving for c (the hypotenuse)?(y/n) ").lower()
    if q == "y":
        a = float(input("What is the value for sidelength a? "))
        b = float(input("What is the value for sidelength b? "))
        c = sqrt(a**2+b**2)
        print("The length of side C is:", c)
    else:
        q2 = float(input("What side are you solving for? (a/b): ")).lower()
        if q2 == "a":
            c = float(input("What is the length of the hypotonuse? "))
            b = float(input("What is the length of side b? "))
            a = sqrt(c**2-b**2)
            print("The length of side A is:",a)
        if q2 == "b":
            c = float(input("What is the length of the hypotonuse? "))
            a = float(input("What is the length of side b? "))
            b = sqrt(c**2-a**2)
            print("The length of side A is:",a)
        
def heronForm(a,b,c):
    s = (a+b+c)/2
    area = sqrt(s*(s-a)*(s-b)*(s-c))
    print("The area of a triangle with sidelenghts: "+str(a)+", "+str(b)+", "+str(c)+", is:", area)



