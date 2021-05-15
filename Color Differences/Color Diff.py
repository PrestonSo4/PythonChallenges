global colorWheel
import math
colorWheel = []

colorWheel.append(["Red",255,0,0])
colorWheel.append(["Orange",255,127,0])
colorWheel.append(["Yellow",255,255,0])
colorWheel.append(["Chartreuse Green",127,255,0])
colorWheel.append(["Green",0,255,0])
colorWheel.append(["Spring Green",0,255,127])
colorWheel.append(["Cyan",0,255,25])
colorWheel.append(["Azure",0,127,255])
colorWheel.append(["Blue",0,0,255])
colorWheel.append(["Violet",127,0,255])
colorWheel.append(["Magenta",255,0,255])
colorWheel.append(["Rose",255,0,127])
def getKey(val, dic):
    for key, value in dic.items():
         if val == value:
             return key
 
    return "key doesn't exist"
def colorDifference():
    results = dict()
    rColor = float(input('Enter the R of the color: '))
    gColor = float(input('Enter the G of the color: '))
    bColor = float(input('Enter the B of the color: '))
    for row in colorWheel:
        difference = math.sqrt(pow((row[1]-rColor), 2) + pow((row[2]-gColor),2) + pow((row[3]-bColor),2))
        results.update({row[0] : difference})
    print(results)
    smallest = min(results.values())
    print(getKey(smallest, results))

colorDifference()