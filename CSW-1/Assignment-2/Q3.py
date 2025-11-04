stack = []   # stack using list

def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        print("Stack is empty! Cannot pop.")
        return None
    return stack.pop()

def is_empty():
    return len(stack) == 0

def display():
    if is_empty():
        print("Stack is empty.")
    else:
        print("Stack (top -> bottom): ", end="")
        for i in range(len(stack)-1, -1, -1):
            print(stack[i], end=" ")
        print()

def evaluate_rpn(expr):
    temp_stack = []
    tokens = expr.split()

    for token in tokens:
        if token.isdigit() or (token[0]=='-' and token[1:].isdigit()):
            temp_stack.append(int(token))
        else:
            b = temp_stack.pop()
            a = temp_stack.pop()

            if token == '+': temp_stack.append(a + b)
            elif token == '-': temp_stack.append(a - b)
            elif token == '*': temp_stack.append(a * b)
            elif token == '/': temp_stack.append(a / b)
            else:
                print("Invalid operator!")
                return

    return temp_stack.pop()


# -------- MENU --------
while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Evaluate RPN")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        val = int(input("Enter value to push: "))
        push(val)
        print("Pushed:", val)

    elif choice == "2":
        val = pop()
        if val is not None:
            print("Popped:", val)

    elif choice == "3":
        display()

    elif choice == "4":
        expr = input("Enter RPN Expression: ")
        result = evaluate_rpn(expr)
        print("Result:", result)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
