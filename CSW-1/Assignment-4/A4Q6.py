import re

pattern = r'^[a-z]+\d+$'

tests = ["abc123", "a1b2", "ABC123"]
for t in tests:
    print(t, "→", "pass" if re.fullmatch(pattern, t) else "fail")
