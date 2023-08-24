print("*****calculator  *****")

num1 = float(input("ENTER A NUMBER HERE"))
num2 = float(input("ENTER ANOTHER NUMBER HERE"))

print("""
      press 1 for addition
      press 2 for subtraction
      press 3 for multiplication
      press 4 for division""" )

choice = int(input("enter a number between 1-4"))

if choice == 1:
    sum = num1+num2
    print("addition is", sum)
elif choice == 2:
    print("substration is", num1-num2)
elif choice ==3:
    print("multiplication is ", num1*num2)
elif choice ==4:
    print("division is", num1/num2)
else:
    print(" INVALID  INPUT")
