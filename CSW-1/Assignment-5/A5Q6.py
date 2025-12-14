import os
from datetime import date
if os.path.exists("diary.txt"):
  print("File already exists. Not overwriting.")
else:
  entry = input("enter diary note : ")
  with open("diary.txt","w") as f:
    f.write(str(date.today()) + "\n")
    f.write(entry)
  print("Diary written successfully.")
try:
    with open("diary.txt", "r") as f:
        print("Diary contents:")
        print(f.read())
except FileNotFoundError:
    print("File not found. Please check the name.")

