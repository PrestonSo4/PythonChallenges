#Actual Code
def EntryFee():
    adults = int(input("How many adults are there: "))
    kids = int(input("How many kids are there: "))
    aPrice = adults * 15
    kPrice = kids * 11
    total = aPrice + kPrice
    if total > 50:
        total *= 0.05
    return total
print(EntryFee())    

print("testing testing 12345")