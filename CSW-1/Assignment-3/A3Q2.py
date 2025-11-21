# q2_cli_calc.py
import sys

print("Simple Command-Line Calculator")
print("Usage: add 5 3   |   sub 10 4   |   mul 2 7   |   div 15 3   |   exit")

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    if line.lower() == "exit":
        print("Program terminated.")
        break

    parts = line.split()
    if len(parts) != 3:
        print("Error: Please enter exactly 3 items: operation num1 num2")
        continue

    op, a_str, b_str = parts

    if op not in ("add", "sub", "mul", "div"):
        print("Error: Invalid operation. Use add, sub, mul, or div.")
        continue

    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        print("Error: Please enter valid numbers.")
        continue

    if op == "add":
        print(f"Result: {a + b}")
    elif op == "sub":
        print(f"Result: {a - b}")
    elif op == "mul":
        print(f"Result: {a * b}")
    elif op == "div":
        if b == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = a / b
            print(f"Result: {int(result) if result == int(result) else result}")
