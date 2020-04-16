#Project Name: Calculator for 2 numbers
#Enter numbers
num1 = float(input("Enter number 1___"))
num2 = float(input("Enter number 2___"))
# Enter operator
operator = input("Enter operator")

if operator == "+":
    print(num1," ",operator," ",num2," =", num1+num2)
elif operator == "-":
    print(num1," ",operator," ",num2," =", num1-num2)
elif operator == "*":
    print(num1," ",operator," ",num2," =", num1*num2)
elif operator == "/":
    print(num1," ",operator," ",num2," =", num1/num2)
else:
    print("Operator not recognized")
## This is my change 1
## This is the second change 2