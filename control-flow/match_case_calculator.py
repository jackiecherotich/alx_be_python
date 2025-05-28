#Ask the user to input the first number
num1=float(input("Enter the first number: ")) 
#Enter the second number:
num2=float(input("Enter the second number: ")) 
           
           # Choose the Type of Operation to perform
operation =input("Choose the operation (+, -, *, /):")
#Operation commands

if operation =='+':
 result = num1 + num2

elif operation =='-':
 result =num1 - num2

elif operation =='*':
 result =num1 * num2



elif operation == '/':
    if num2 == 0:
        result = "Error: Cannot divide by zero"
    else:
        result = num1 / num2
else:
    result = "Invalid operation selected"


print("The result is " ,result,)