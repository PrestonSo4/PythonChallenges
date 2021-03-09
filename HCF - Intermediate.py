a = float(input("Enter the larger of the numbers: "))
b = float(input("Enter the smaller of the numbers: "))
while b > 0:
    temp = b
    b = a%b
    a = temp
print(a)

"""
a = 96
b = 36
------
temp = 36
b = 24
a = 36
------
temp = 24
b = 12
a = 24
------
temp = 12
b = 0
a = 12
"""