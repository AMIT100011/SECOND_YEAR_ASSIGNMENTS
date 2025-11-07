# q2_cli_calc.py
print("Enter: op num1 num2 where op in {add, sub, mul, div}. Type 'exit' to quit.")
while True:
    line = input().strip()
    if line.lower() == "exit":
        print("Program terminated.")
        break

    parts = line.split()
    if len(parts) != 3:
        print("Format: op num1 num2")
        continue

    op = parts[0].lower()
    try:
        a = float(parts[1])
        b = float(parts[2])
    except ValueError:
        print("Error: invalid numbers.")
        continue

    if op == "add":
        result = a + b
    elif op == "sub":
        result = a - b
    elif op == "mul":
        result = a * b
    elif op == "div":
        if b == 0:
            print("Error: Division by zero is not allowed.")
            continue
        result = a / b
    else:
        print("Error: unknown operation.")
        continue

    if result == int(result):
        result = int(result)
    print("Result:", result)
