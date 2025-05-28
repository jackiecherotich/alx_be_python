#Ask the user to input the first number
num1=float(input("Enter the first number: ")) 
#Enter the second number:
num2=float(input("Enter the second number: ")) 
           
           # Choose the Type of Operation to perform
operation =input("Choose the operation (+, -, *, /):")
#Operation commands

match operation:
    case "+":
        result = num1 + num2
        print("The result is ",result,)
    case "-":
        result = num1 - num2
        print("The result is ",result,)
    case "*":
        result = num1 * num2
        print("The result is ",result,)
    case "/":
        if num2 != 0:
            result = num1 / num2
            print("The result is ",result,)
        else:
            print("Error: Cannot divide by zero.")
    case _:
        print("Invalid operation. Please choose one of +, -, *, /.")

