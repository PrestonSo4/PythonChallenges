#https://www.101computing.net/school-trip-bus-quote/
# Large Bus: $360 Small Bus: $140
smallBus = 140
bigBus = 360
sBLimit = 16
bBLimit = 46
def calculateBus():
    students = int(input('Enter the number of students: '))
    staff = int(input('Enter the number of staff: '))
    participants = students + staff
    bigBuses = participants // bBLimit
    remainder = round(participants % bBLimit)
    smallBuses = remainder // sBLimit
    remainder = round(remainder % sBLimit)
    if remainder > 0:
        smallBuses += 1
    print('Small buses:', smallBuses)
    print('Big Buses:', bigBuses)
    totalCost = smallBuses * 140 + bigBuses * 360
    print('Total Cost:', totalCost)

calculateBus()
