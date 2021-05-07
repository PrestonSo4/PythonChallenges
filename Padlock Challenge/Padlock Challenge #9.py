#https://www.101computing.net/padlock-code-challenge-9/
def isPrime(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    
    return prime
number = 0
code = 0
for i in range(2, 999): # 0 and 1 are not prime numbers so that's why it wasn't working
    if isPrime(i):
        code += i
        number += 1
        print(i, '\n')
        print(code, '\n')
print(code)
code = round(code/number)
print(number)
print('Code:', code)