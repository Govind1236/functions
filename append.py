user_input = input("Enter a Number: ")
# split string into individual numbers
number_list = user_input.split()

# change string to float
number_list = [float(num) for num in number_list]
average = sum(number_list) / len(number_list)
print("The average is:", average)

