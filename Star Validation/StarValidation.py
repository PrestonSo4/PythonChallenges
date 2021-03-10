#Starting
def validate(start,end):
    rating = float(input(f"What will be your rating today ({start}-{end}): "))
    while rating > end or rating < start:      
        print("That is not within the range. Try again")
        rating = float(input(f"What will be your rating today ({start}-{end}): "))
        
    print("Thank you for your input. We hope to see you again")
validate(1,5)