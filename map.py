#MAP 
def cube(x):
    return x * x * x
l = [1 ,4 , 8 , 50 ]
# new = []
# for i in l:
#     new.append(cube(i))
# print(new)
print(list(map(cube, l)))

# Filter
def filter_function(a):
    return a > 3
print(list(filter(filter_function, l)))
