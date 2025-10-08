# Function to count vowels in the text
def count_vowels(text):
    vowels = "AEIOU"
    counts = {v: 0 for v in vowels}

    for ch in text.upper():
        if ch in vowels:
            counts[ch] += 1

    return counts


# Main program
paragraph = input("Enter a paragraph: ")

# Remove extra spaces using split() and join()
cleaned = " ".join(paragraph.split())

# Convert to title case
title_case = cleaned.title()

# Count vowels
vowel_counts = count_vowels(title_case)

# Display results
print("\nProcessed Text:", title_case)
print("\nVowel Counts:")
for vowel, count in vowel_counts.items():
    print(f"{vowel} (char code {ord(vowel)}): {count}")
