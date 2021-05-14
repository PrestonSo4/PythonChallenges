#https://www.101computing.net/padlock-code-challenge-3/

def findInstance():
    code = 0
    for i in range(10):
        for i2 in range(10):
            for i3 in range(10):
                if i % 2 == 0 and i2 % 2 == 0 and i3 % 2 == 0:
                    code += 1
    return code
print(findInstance())