#https://www.101computing.net/linear-search-functions/

def readFile(filename):
    lst = list()
    file = open(filename, "r") #Opens file in read-only mode("r") 
    for value in file:
        lst.append(value.rstrip("\r\n")) #The value.rstrip strips all the items specified in the ""s. \r is carrage returns and \n is newlines 
    file.close()# Closes the file
    return lst

def isListed(value, lst):
    found = False
    for item in lst:
        if item == value:
            found = True
            break
    return found

#Main Program:

students = readFile('rewards.txt')
student = input("Enter the name of the student you want to find: ")

if isListed(student, students):
    print("The student:", student, "receivied a reward this term!")
else:
    print("The student:", student, "didn't receive a reward this term. :(")

