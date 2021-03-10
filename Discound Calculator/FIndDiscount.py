price = float(input('Enter the price of the item (Without "$"): '))
discountRate = float(input('Enter the percentage rate (Ex) 34% = 34): '))
discount = price * (discountRate / 100)
discountPrice = price - discount
print('Original Price:', price)
print('Discount Rate:', str(discountRate) + "%")
print('Final Price: $'+str(discountPrice))