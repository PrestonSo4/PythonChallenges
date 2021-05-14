##https://www.101computing.net/padlock-code-challenge-1/

def findInstance():
    code = 0
    for i in range(41):
        code += i
    return code
print(findInstance())