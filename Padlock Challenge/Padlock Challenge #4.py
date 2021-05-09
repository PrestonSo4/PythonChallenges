##https://www.101computing.net/padlock-code-challenge-4/
def findInstance():
    code = 0
    for i in range(0,10):
        for i2 in range(0,10):
            for i3 in range(0,10):
                num = i*100 + i2*10 + i3 
                if num % 2 != 0 :
                    code += 1
    return code
print('Code:', findInstance())
