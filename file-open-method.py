f = open("myfile.txt", 'r')
i = 0
while True:
    line = f.readline()
    i = i + 1
    if not line:
        break
    m1 = line.split(",")[0]
    print(f"The marks of student {i} in subjects {m1}")
        
        