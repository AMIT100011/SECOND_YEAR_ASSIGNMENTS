import random
students = ["John", "Riya", "Meera", "Amit",
            "Rahul", "Zara", "Sneha", "Kunal"]
random.shuffle(students)
Team = {"Team A": [], "Team B": [], "Team C": [], "Team D": []}

Team["Team A"].append(students[:2])
Team["Team B"].append(students[2:4])
Team["Team C"].append(students[4:6])
Team["Team D"].append(students[6:8])
for team in Team:
    print(f"{team}: {Team[team]}")

# teams = ["A", "B", "C", "D"]

# for i in range(4):
#     print("Team", teams[i], ":", students[2*i], ",", students[2*i+1])