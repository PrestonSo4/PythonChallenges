from math import sqrt
code = ''
for i in range(999, 0, -1):
    print(i)
    if sqrt(i).is_integer():
        code = i
        break
        
print('Code :', code)