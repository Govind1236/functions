def fun(f , value):
    return 5 + f(value)
double = lambda x: x * x * x
print(double(4))
avg = lambda x, y : (x + y) / 2
print(avg(3, 5))
print(fun(double, 5))