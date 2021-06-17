#www.101computing.net/proportions-and-cross-products


a = int(input("Enter the numerator of your first fraction "))
b = int(input("Enter the denominator of your first fraction "))
print("Fraction #1: " + str(a) + "/" + str(b))
c = int(input('Enter the numerator of the second fraction: '))
d = int(input('Enter the denominator of the second fraction: '))
print('Fraction #2:', str(c) + '/' + str(d))
#Complete the code here to input the second fraction
if a*d == b*c:
    print('The two fractions are proportional')
else:
    print('The two fractions are not proportional')