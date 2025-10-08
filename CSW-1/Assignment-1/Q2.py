# Simple Calculator using if-elif statements

# Take operation choice from user
operation = input("Enter operation (add/sub/mul/div/mod): ").strip().lower()

# Take two numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculation based on choice
if operation == "add":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif operation == "sub":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif operation == "mul":
    result = num1 * num2
    print(f"Result: {num1} × {num2} = {result}")

elif operation == "div":
    if num2 == 0:
        print("Error: Division by zero not allowed.")
    else:
        result = num1 / num2
        print(f"Result: {num1} ÷ {num2} = {result}")

elif operation == "mod":
    if num2 == 0:
        print("Error: Modulus by zero not allowed.")
    else:
        result = num1 % num2
        print(f"Result: {num1} % {num2} = {result}")

else:
    print("Invalid operation! Please choose from add, sub, mul, div, or mod.")
