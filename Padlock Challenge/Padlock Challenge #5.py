#https://www.101computing.net/padlock-code-challenge-5/
def findInstance():
    code = 0
    for i in range(0,10):
        for i2 in range(0,10):
            for i3 in range(0,10):
                if i == i2 or i == i3 or i2 == i3:
                    code += 1
    return code
print('Code:', findInstance())
