#www.101computing.net/my-weekly-timetable/


def whatLesson():
    timetable = []

    #Monday
    timetable.append(["History","Maths","Computer Science","PE","Music"])
    #Tuesday
    timetable.append(["English","Spanish","Maths","Geography","Art"])
    #Wednesday
    timetable.append(["PE","English","Science","Art","PE"])
    #Thursday
    timetable.append(["Maths","English","Philosohpy","Spanish","Music"])
    #Friday
    timetable.append(["Science","Drama","History","Geography","Science"])

    day = int(input('Enter the day(1/2/3/4/5): '))
    day -= 1
    per = int(input('Enter the period: '))
    per -= 1
    print(timetable[day][per])
whatLesson()
def todaysLessons():
    timetable = []

    #Monday
    timetable.append(["History","Maths","Computer Science","PE","Music"])
    #Tuesday
    timetable.append(["English","Spanish","Maths","Geography","Art"])
    #Wednesday
    timetable.append(["PE","English","Science","Art","PE"])
    #Thursday
    timetable.append(["Maths","English","Philosohpy","Spanish","Music"])
    #Friday
    timetable.append(["Science","Drama","History","Geography","Science"])

    day = int(input('Enter the day(1/2/3/4/5): '))
    day -= 1 
    print(timetable[day])
todaysLessons()
def lessonNum():
    timetable = []

    #Monday
    timetable.append(["History","Maths","Computer Science","PE","Music"])
    #Tuesday
    timetable.append(["English","Spanish","Maths","Geography","Art"])
    #Wednesday
    timetable.append(["PE","English","Science","Art","PE"])
    #Thursday
    timetable.append(["Maths","English","Philosohpy","Spanish","Music"])
    #Friday
    timetable.append(["Science","Drama","History","Geography","Science"])
    count = 0
    sub = input('Enter the subject: ')
    for item in timetable:
        if sub in item:
            count+=1
            
lessonNum()