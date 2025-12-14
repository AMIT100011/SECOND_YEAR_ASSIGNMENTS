import re

def verify_passwd(s):
    cond1 = re.fullmatch(r'[A-Za-z0-9@#$%^&*!]{8,}', s)
    cond2 = re.search(r'[0-9]', s)
    cond3 = re.search(r'[A-Za-z]', s)
    cond4 = re.search(r'[@#$%^&*!]', s)

    return cond1 and cond2 and cond3 and cond4

# Test cases
passwords = ["Abc@1234", "abc123", "ABC@1234", "Abcdefg@", "Ab1@defg"]
for p in passwords:
    print(p, ":", bool(verify_passwd(p)))
