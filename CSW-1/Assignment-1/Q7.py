import string

# Step 1: Take input from user
sentence = input("Enter a sentence: ")
separator = input("Enter a custom separator: ")

# Step 2: Remove punctuation from the sentence
cleaned_sentence = ""
for char in sentence:
    if char not in string.punctuation:
        cleaned_sentence += char

# Step 3: Split the cleaned sentence into words
words = cleaned_sentence.split()

# Step 4: Convert all words to lowercase for uniform sorting
words = [word.lower() for word in words]

# Step 5: Sort words in reverse alphabetical order
words.sort(reverse=True)

# Step 6: Join words using the custom separator
result = separator.join(words)

# Step 7: Display the result
print("\nSorted words (reverse alphabetical):")
print(result)
