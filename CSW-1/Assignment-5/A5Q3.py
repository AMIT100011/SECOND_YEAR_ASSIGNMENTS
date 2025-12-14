poem = [
    "Roses are red,\n",
    "Violets are blue,\n",
    "Python is fun,\n",
    "And so are you.\n"
]

with open("poem.txt", "w") as file:
    file.writelines(poem)

print("Poem written to file successfully.")

with open("poem.txt", "r") as file:
    print("Reading back from poem.txt:")
    for line in file:
        print(line, end="")
