import string

# Function to count word frequencies
def word_frequency(sentence):
    # Remove punctuation
    cleaned = "".join(ch for ch in sentence if ch not in string.punctuation)

    # Convert to lowercase and split into words
    words = cleaned.lower().split()

    # Count frequencies
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    return freq

# Main program
sentence = input("Enter a sentence: ")
freq_dict = word_frequency(sentence)

# Sort words alphabetically
sorted_words = sorted(freq_dict.items())

# Display result
print("\nWord Frequencies:")
for word, count in sorted_words:
    print(f"{word}: {count}")
