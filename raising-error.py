input = int(input("Enter a number: "))

if input < 10 or input > 15:
    raise ValueError("Choose between 10 to 15")
    
print("Execute")
