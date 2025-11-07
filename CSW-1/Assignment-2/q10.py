def is_prime(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def process_dict(data):
    new_dict = {}

    for key in data:
        value = data[key]

        # If value is a list → sum of primes
        if type(value) == list:
            total = 0
            for x in value:
                if is_prime(x):
                    total += x
            new_dict[key] = total

        # If value is a tuple → product of odd numbers
        elif type(value) == tuple:
            product = 1
            has_odd = False
            for x in value:
                if x % 2 != 0:     # odd number
                    product *= x
                    has_odd = True
            # if no odd number, keep product as 0
            if has_odd:
                new_dict[key] = product
            else:
                new_dict[key] = 0

    return new_dict


# ---- Example Input ----
data = {
    "A": [2, 3, 4, 5, 10],
    "B": (1, 2, 3, 4, 5),
    "C": [7, 8, 9],
    "D": (6, 7, 8)
}

# ---- Function Call ----
result = process_dict(data)

# ---- Output ----
print("Output Dictionary:")
print(result)
