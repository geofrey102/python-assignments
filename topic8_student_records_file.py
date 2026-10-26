f = open("students.txt", "w")

print("Alice, UNI001, Computer Science, 85", file=f)
print("Brian, UNI002, Information Technology, 78", file=f)
print("Catherine, UNI003, Software Engineering, 92", file=f)

f.close()

print("Student records saved successfully.")
print("Opening an existing file in w mode erases its previous contents.")
