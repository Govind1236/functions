def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) +(n - 2)
c = int(input("Enter a number: "))
result = []
for i in range(c):
    result.append(fibonacci(i))
print("the series is: ", result)

# 0 1 2 3 4
# 0 , 1 ,1 ,3, 5


