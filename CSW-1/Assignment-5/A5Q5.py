with open("hello.txt", "r") as file:
    first_ten = file.read(10)
    print("First 10 characters:", first_ten)

    file.seek(0)   # move pointer to beginning
    print("Full file contents after seek():")
    print(file.read())
