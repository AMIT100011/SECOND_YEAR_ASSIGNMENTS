import struct

numbers = [10, 20, 30, 40, 50]

with open("numbers.bin", "wb") as file:
    for num in numbers:
        file.write(struct.pack("i", num))

print("Integers written to binary file successfully.")

read_numbers = []
with open("numbers.bin", "rb") as file:
    while True:
        data = file.read(4)
        if not data:
            break
        read_numbers.append(struct.unpack("i", data)[0])

print("Integers read from file:", read_numbers)
