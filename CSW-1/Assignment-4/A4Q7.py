import re

text = "Random <tag>first</tag> some text <tag>second</tag> end"

# (a) Greedy
print(re.search(r'<tag>.*</tag>', text).group())

# (b) Non-greedy
matches = re.findall(r'<tag>.*?</tag>', text)
print(matches)
