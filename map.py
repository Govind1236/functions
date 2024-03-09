def cube(x):
    return x * x * x
l = [1 ,4 , 8 , 50 ]
# new = []
# for i in l:
#     new.append(cube(i))
# print(new)
print(list(map(cube, l)))
