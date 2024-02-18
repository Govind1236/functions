# name = ["Govind", 902 , "Awesome"]
# index = 0
# for letter in name:
#     if (index == 1):
#         print("Wow its", letter) 
#     index += 1
name = ["Govind", 902 , "Awesome"]
try:
    index = int(input("Enter a Number: "))
    if index > 0 or index < len(name):
        print(f"The value in {index} index is", name[index])
    else:
        print("Index out of range")
except:
    print("Error occurs")