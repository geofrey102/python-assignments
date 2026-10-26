student = {
    "registration_number": "UNI001",
    "name": "Alice Wanjiku",
    "course": "Computer Science",
    "year_of_study": 1
}

print("Student Name:", student["name"])
print("Course:", student["course"])

student["year_of_study"] = 2
student["email"] = "alice@example.com"

print("Updated Student Record:", student)
