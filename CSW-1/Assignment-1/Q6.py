# Function to encrypt the string
def encrypt(text):
    # Step 1: Reverse the string
    reversed_text = text[::-1]

    # Step 2: Swap every adjacent pair of characters
    chars = list(reversed_text)
    for i in range(0, len(chars) - 1, 2):
        chars[i], chars[i + 1] = chars[i + 1], chars[i]

    encrypted = ''.join(chars)
    return encrypted


# Function to decrypt the string
def decrypt(encrypted_text):
    # Step 1: Swap back every adjacent pair of characters
    chars = list(encrypted_text)
    for i in range(0, len(chars) - 1, 2):
        chars[i], chars[i + 1] = chars[i + 1], chars[i]

    # Step 2: Reverse the string again to get original
    decrypted = ''.join(chars)[::-1]
    return decrypted


# Main program
text = input("Enter a string: ")

encrypted_text = encrypt(text)
decrypted_text = decrypt(encrypted_text)

# Display results
print(f"\nEncrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
