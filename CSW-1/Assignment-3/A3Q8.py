# sumargs.py
import sys

args = sys.argv[1:]
if len(args) == 0:
    print("Usage: python sumargs.py <num1> <num2> ...")
else:
    total = 0.0
    valid = True
    for token in args:
        try:
            total += float(token)
        except ValueError:
            print("Error: Invalid input '", token, "'. Please enter only numbers.", sep="")
            valid = False
            break
    if valid:
        if total == int(total):
            total = int(total)
        print("Sum of numbers:", total)
