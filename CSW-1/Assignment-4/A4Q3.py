import re

def normalize_phones(s):
    pattern = r'(?:\+91[- ]?|\(91\) ?|0091 ?|91 ?)(\d{10})'
    return re.sub(pattern, r'+91-\1', s)
text = "Contact: +91-9876543210, Office: (91) 9876543210, Home: 0091 9876543210"
print(normalize_phones(text))
