def sum_of_digits(num):
    if num == 0:
        return num
    else:
        return num % 10 + sum_of_digits(num // 10)
n1 = float(input("Enter a number: "))
result = sum_of_digits(n1)
print("The sum is: ",result)    