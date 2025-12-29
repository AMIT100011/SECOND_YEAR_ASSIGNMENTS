import random
import string
freq ={}
for i in range(100):
  ch = random.choice(string.ascii_lowercase)
  freq[ch] = freq.get(ch, 0) + 1
for k in freq:
  print(f"Character {k}: Frequency = {freq[k]}, Probability = {freq[k]/100:.3f}")