students = ["Alice", "Bob", "Charlie", "David", "Eva"]

with open("students.txt","w") as f:
  for name in students:
    f.write(name+ "\n")

print("File 'students.txt' created successfully.")

with open("students.txt","r") as f:
  print(f.read())
