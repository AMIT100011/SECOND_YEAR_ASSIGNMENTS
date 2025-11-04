def top_student():
    students_scores = {}
    
    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input("\nEnter student name: ")
        scores = []
        
        m = int(input("Enter number of scores for " + name + ": "))
        
        for j in range(m):
            score = int(input(f"Enter score {j+1}: "))
            scores.append(score)     # using list append()
        
        students_scores[name] = scores

    # Find student with highest average
    topper = ""
    highest_avg = -1

    for name in students_scores:
        scores = students_scores[name]
        
        # Calculate average using list methods
        total = 0
        for marks in scores:
            total += marks

        avg = total / len(scores)   # using len()

        if avg > highest_avg:
            highest_avg = avg
            topper = name

    print("\nTop student based on average score:", topper)


# Call function
top_student()
