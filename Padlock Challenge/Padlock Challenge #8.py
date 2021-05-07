#https://www.101computing.net/padlock-code-challenge-8/
def isPrime(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    
    return prime
code = ''
for i in range(2, 999): # 0 and 1 are not prime numbers so that's why it wasn't working
    if isPrime(i):
        print(i, '\n')
        code = i
print('Code:', code)