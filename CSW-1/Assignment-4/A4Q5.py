import re

def check_word(word):
    return bool(re.fullmatch(r'c[aeiou][^aeiou]', word))

# Test
tests = ["cat", "cit", "cot", "cut", "caa"]
for t in tests:
    print(t, check_word(t))
