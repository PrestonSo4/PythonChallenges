#https://www.101computing.net/padlock-code-challenge-6/
def findInstance():
    code = 0
    for d1 in range(0,10):
        for d2 in range(0,10):
            for d3 in range(0,10):
                if d1 + d2 == d3 or d1 + d3 == d2 or d3 + d2 == d1:
                    print(str(d1)+str(d2)+str(d3))
                    code += 1
    return code

print(findInstance())
