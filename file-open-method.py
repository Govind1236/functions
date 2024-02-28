# f = open("myfile.txt", 'r')
# i = 0
# while True:
#     line = f.readline()
#     i = i + 1
#     if not line: 
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"The marks of student {i} in subjects {m1}")
#     print(f"The marks of student {i} in subjects {m2}")
#     print(f"The marks of student {i} in subjects {m3}")

#     print(line)
with open('myfile.txt','w') as f:
    file = f.write("okay")
    f.truncate(2)
    with open('myfile.txt', 'r') as f:
        print(f.read())
    # print(f.tell())
    # print(file)