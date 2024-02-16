user_input = input("Enter a Name: ")
names = user_input.split(" ")
while_coding = True
if(while_coding):
    nam = []
    for name in names:
     if(len(user_input) >= 3):
       rand = "adf"
       rand1 = "qrt"
       user_input = rand + name[1:] + name[0] + rand1
       nam.append(user_input)
    else:
      nam.append(name[::-1])
    print("".join(nam))
else:
   nam = []
   for name in names:
    if(len(user_input) >= 3):
      name = nam[-1] + nam[:-1]
      user_input = name[3:] 
      nam.append(user_input)
    else:
    #   nam.append(name[::-1])
     print("".join(nam))