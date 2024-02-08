list1 = [1, 1, 1, 2, 2, 3, 4, 2, 4, 5, 6]
reapeat_dict = {}
for num in list1:
    if num in reapeat_dict:
        reapeat_dict[num] += 1
    else:
        reapeat_dict[num] = 1
print("The repeated number is: ")
for num , score in reapeat_dict.items():
    if score > 1:
     print(f"{num}: {score}")


 
