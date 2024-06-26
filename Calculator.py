# Function to perform the arithmetic operations
def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation choice."

# Main function
def main():
    # Prompt the user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt the user to choose an operation
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")

    # Perform the calculation and display the result
    result = calculate(num1, num2, operation)
    print(f"The result is: {result}")

# Run the main function
if __name__ == "__main__":
    main()
