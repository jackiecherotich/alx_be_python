# main.py

from arithmetic_operations import perform_operation

def main():
    print("Basic Arithmetic Operations")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()

        result = perform_operation(num1, num2, operation)

        if isinstance(result, str) and result.startswith("Error"):
            print(result)
        else:
            print(f"The result is: {result}")

    except ValueError:
        print("Error: Please enter valid numerical values.")

if __name__ == "__main__":
    main()
