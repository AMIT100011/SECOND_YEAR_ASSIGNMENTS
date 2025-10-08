# Program: Multi-base conversion of a decimal number

# Step 1: Read decimal number from user
decimal_num = int(input("Enter a decimal number: "))

# Step 2: Convert to binary, octal, and hexadecimal (without prefixes)
binary_str = bin(decimal_num)[2:]      # remove '0b'
octal_str = oct(decimal_num)[2:]       # remove '0o'
hex_str = hex(decimal_num)[2:].upper() # remove '0x' and make uppercase

# Step 3: Display converted values and digit counts
print("\n--- Base Conversions ---")
print(f"Binary       : {binary_str}  (Digits: {len(binary_str)})")
print(f"Octal        : {octal_str}  (Digits: {len(octal_str)})")
print(f"Hexadecimal  : {hex_str}  (Digits: {len(hex_str)})")

# Step 4: Reverse conversion using int(string, base)
re_binary = int(binary_str, 2)
re_octal = int(octal_str, 8)
re_hex = int(hex_str, 16)

# Step 5: Display reverse conversion results
print("\n--- Reverse Conversion Verification ---")
print(f"From Binary      → Decimal: {re_binary}")
print(f"From Octal       → Decimal: {re_octal}")
print(f"From Hexadecimal → Decimal: {re_hex}")
