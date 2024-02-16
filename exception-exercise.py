# Write a Python program that takes two numbers as input from the user and performs division
# on them. However, you should handle the possibility of division by zero and any other unexpected error
# s gracefully using exception handling.
def divison():
 while True:
    try:
        num = float(input("Enter First Number: "))
        num1 = float(input("Enter Second Number: "))

        divide = num / num1
        print(divide)
    except ValueError:
        print("The value error occured")
    except ZeroDivisionError:
        print("Error: Division By Zero is not allowed")
    except Exception as b:
        print("Unexpected Error occur", b)
    finally:
       print("Im executed")

    user_choice = input("Do you want to continue? (yes/no): ").strip().lower()
    if user_choice == "no":
      print("The loop Ends here")
      break
       
divison()