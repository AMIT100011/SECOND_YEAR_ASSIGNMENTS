import random

count = {i:0 for i in range(2, 13)}
for i in range(10000):
  d1 = random.randint(1, 6)
  d2 = random.randint(1, 6)
  total = d1 + d2
  count[total] += 1

for i in count:
  print(f"Sum {i}: Frequency = {count[i]}, Probability = {count[i]/10000:.3f}")

