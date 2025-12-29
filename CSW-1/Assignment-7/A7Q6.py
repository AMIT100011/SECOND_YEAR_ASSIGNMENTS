import random
count = [0]*6
for i in range(2000):
  res = random.randint(1,6)
  count[res-1] += 1
for i in count:
  print(f"Face {count.index(i)+1}: Frequency = {i}, Probability = {i/2000:.3f}")
print("Highest:", count.index(max(count)) + 1)
print("Lowest:", count.index(min(count)) + 1)
