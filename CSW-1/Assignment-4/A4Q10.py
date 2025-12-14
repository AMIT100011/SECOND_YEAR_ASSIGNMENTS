import re

def find_repeated_letters(s):
    pattern = r'(.)\1+'
    for m in re.finditer(pattern, s):
        print("Repeated sequence:", m.group(0))
        print("Character:", m.group(1))
        print("Span:", m.span())
        print()

# Test
find_repeated_letters("baallooon missssion zzzz")
