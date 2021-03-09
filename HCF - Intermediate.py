a = float(input("Enter the larger of the numbers: "))
b = float(input("Enter the smaller of the numbers: "))
while b > 0:
    temp = b
    b = a%b
    a = temp
print(a)