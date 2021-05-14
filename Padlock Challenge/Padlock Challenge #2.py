##https://www.101computing.net/padlock-code-challenge-2/

def findInstance():
    code = 0
    for i in range(10):
        for i2 in range(10):
            for i3 in range(10):
                if i < i2 and i2 < i3:
                    code += 1
    return code
print(findInstance())