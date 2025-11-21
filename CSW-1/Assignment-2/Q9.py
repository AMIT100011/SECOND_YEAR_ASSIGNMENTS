# Input: List of tuples (name, age, nationality)
voters = [
    ("Amit", 22, "Indian"),
    ("John", 30, "USA"),
    ("Neha", 17, "Indian"),
    ("Ravi", 19, "Indian"),
    ("Priya", 16, "Indian"),
    ("Alex", 25, "UK"),
    ("Suresh", 20, "Indian")
]

# Step 1: Use filter() to get eligible voters (age >= 18 AND Indian)
eligible_voters = list(filter(lambda voter: voter[1] >= 18 and voter[2] == "Indian", voters))

# Extract only names of eligible voters
eligible_names = [voter[0] for voter in eligible_voters]

# Step 2: Count total eligible voters
total_eligible = len(eligible_names)

# Step 3: Dictionary comprehension to group eligible and not eligible
result_dict = {
    "Eligible": [voter[0] for voter in voters if voter[1] >= 18 and voter[2] == "Indian"],
    "Not Eligible": [voter[0] for voter in voters if not (voter[1] >= 18 and voter[2] == "Indian")]
}

# Display results
print("Eligible:", eligible_names)
print("Count:", total_eligible)
print(result_dict)
