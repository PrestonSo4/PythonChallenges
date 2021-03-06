#Starting
start = 1
end = 5
rating = float(input(f"What will be your rating today ({start}-{end}): "))

def validate(rating,start,end):
    while rating > end or rating < start:      
        print("That is not within the range. Try again")
        rating = float(input(f"What will be your rating today ({start}-{end}): "))
        
    print("Thank you for your input. We hope to see you again")
validate(rating,start,end)