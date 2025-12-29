import random
import string
for i in range(10):
  str = ""
  for j in range(8):
    str += random.choice(string.ascii_lowercase)
  print(str)