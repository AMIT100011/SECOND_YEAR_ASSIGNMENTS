text = "Python"

with open("strings.txt", "wb") as file:
    file.write(text.ljust(20).encode())  # fixed length
    file.write(text.encode())            # variable length

with open("strings.txt", "rb") as file:
    fixed = file.read(20)
    variable = file.read()

print("Fixed length storage:", fixed.decode(), "(20 bytes)")
print("Variable length storage:", variable.decode(), "(6 bytes)")
