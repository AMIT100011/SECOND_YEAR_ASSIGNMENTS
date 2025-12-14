import pickle

students = {
    "Alice": (20, "A"),
    "Bob": (19, "B"),
    "Charlie": (21, "A")
}

with open("students.pkl", "wb") as file:
    pickle.dump(students, file)

print("Pickled data saved successfully.")

with open("students.pkl", "rb") as file:
    data = pickle.load(file)

print("Unpickled data:", data)
