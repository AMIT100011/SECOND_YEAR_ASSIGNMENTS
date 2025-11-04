score = []

n = int(input("Enter the number of students: "))
for i in range(n):
    student = float(input(f"Enter the marks of student {i+1}: "))
    score.append(student)
sum = 0
for i in score:
  sum += i
average = sum / n
print(f"the average is {average}")

print("------------------------------")

maximum = score[0]
minimum = score[0]

for i in score:
  if i < minimum:
    minimum = i
  if i > maximum:
    maximum = i
print(f"Minimum score: {minimum}")
print(f"Maximum score: {maximum}")

print("------------------------------")

print("Scores above average:")
above_avg = [s for s in score if s > average]
print(above_avg)

print("------------------------------")

print(sorted(score,reverse=True))

# for i in range(len(temp_scores)):
#     for j in range(i+1, len(temp_scores)):
#         if temp_scores[i] > temp_scores[j]:
#             temp_scores[i], temp_scores[j] = temp_scores[j], temp_scores[i]
print("------------------------------")

print(sorted(score))
print(score[3:])
