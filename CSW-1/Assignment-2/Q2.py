import math

# Function to check prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to classify numbers
def classify_numbers(numbers):
    result = {
        "Prime Numbers": [],
        "Composite Numbers": [],
        "Perfect Squares": [],
        "Perfect Cubes": []
    }
    
    for n in numbers:
        # Prime Check
        if is_prime(n):
            result["Prime Numbers"].append(n)
        elif n > 1:  # Composite check (greater than 1 and not prime)
            result["Composite Numbers"].append(n)
        
        # Perfect Square Check
        if int(math.sqrt(n)) ** 2 == n:
            result["Perfect Squares"].append(n)
        
        # Perfect Cube Check
        if round(n ** (1/3)) ** 3 == n:
            result["Perfect Cubes"].append(n)

    return result


# Taking input from user
nums = list(map(int, input("Enter integers separated by space: ").split()))

# Display result
output = classify_numbers(nums)
print("\nClassification Result:")
for category, values in output.items():
    print(f"{category}: {values}")
