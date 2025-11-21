# Step 1: Input list with duplicates
numbers = [4, 2, 7, 4, 2, 4, 9, 7, 9, 9]

# Step 2: Remove duplicates using SET COMPREHENSION
unique_numbers = {x for x in numbers}  # or simply: set(numbers)
print("Unique numbers:", sorted(unique_numbers))

# Step 3: Build frequency dictionary using DICTIONARY COMPREHENSION
freq_dict = {num: numbers.count(num) for num in unique_numbers}
print("Frequency dictionary:", freq_dict)

# Step 4: Sort numbers by frequency (descending) using lambda + sorted()
sorted_by_freq = sorted(unique_numbers, key=lambda x: freq_dict[x], reverse=True)

# Final Output
print("\nNumbers sorted by frequency (descending):")
for num in sorted_by_freq:
    print(f"{num} → appears {freq_dict[num]} time(s)")

# Bonus: Show only the top frequency ones (optional)
print("\nTop most frequent:", sorted_by_freq[0])
