try:
    with open("data.txt", "r") as file:
        print("File opened successfully.")
        print("Contents of data.txt:")
        print(file.read())
except FileNotFoundError:
    print("Error: File not found.")
    
