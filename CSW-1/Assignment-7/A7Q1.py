import random
heads = 0
tails = 0
for i in range(1, 1000):
    flip = random.choice(['H', 'T'])
    if flip == 'H':
        heads += 1
    else:
        tails += 1
print("Number of heads:", heads)
print("Number of tails:", tails)
print("probability of heads:", heads / 1000)
print("probability of tails:", tails / 1000)