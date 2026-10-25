marks = [75, 82, 69, 90, 88]

print("All Marks:", marks)

total_marks = sum(marks)
average_mark = total_marks / len(marks)

print("Total Marks:", total_marks)
print("Average Mark:", average_mark)
print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks))

marks[2] = 85

print("Updated Marks:", marks)
