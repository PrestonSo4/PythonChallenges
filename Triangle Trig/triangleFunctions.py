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
    if a = b and a = c:
        print("The triangle with all sidelengths of:", a, "is an equilateral triangle.")
    else:
        print("Your triangle with the specified information is not an equilateral tirangle")
def isIsoscles(a,b,c):
    if a == b or a == c or b == c:
        print("A triangle with the sideslengths of:",str(a) + ",",str(b) + ",",str(c) + ", is an Isoscles triangle.")
    else:
        print("Your triangle with the specified information is not an isoscles tirangle")        
