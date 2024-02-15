# try:
#    num = int(input("Enter a number: "))
#    for i in range(num):
#     # i = i + 1
#     print(i)
# except:
#    print("invalid Input")
# print("Enter valid int not a string")

try:
   num = int(input("Enter a number: "))
   a = [5 , "g"]
   print(a[num])
except ValueError:
   print("Enter number is not integer")
except IndexError:
   print("index Error")