import re

def find_upper_digit(s):
    m = re.search(r'([A-Z]).*\d', s)
    if m:
        return m.group(1), m.start(1)

# Test
print(find_upper_digit("a B blah 9"))
