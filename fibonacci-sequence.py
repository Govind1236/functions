def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
c = int(input("Enter a number: "))
result = []
for i in range(c):
    result.append(fibonacci(i))
print("the series is: ", result)



