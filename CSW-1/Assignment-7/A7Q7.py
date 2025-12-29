import random
deck = list(range(1, 53))
random.shuffle(deck)
deal = deck[:5]
print(deal)